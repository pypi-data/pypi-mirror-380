"""Agent Interface class and methods for interaction with Jivas."""

import logging
import os
import traceback
from typing import Any

import requests
from fastapi import Request
from fastapi.responses import JSONResponse

from jvserve.lib.jac_interface import JacInterface


class AgentInterface:
    """Agent Interface for Jivas with proper concurrency handling."""

    _instance = None
    logger = logging.getLogger(__name__)
    timeout = int(os.environ.get("JIVAS_REQUEST_TIMEOUT", 30))

    def __init__(self, host: str = "localhost", port: int = 8000) -> None:
        """Initialize the AgentInterface with JacInterface."""
        self._jac = JacInterface(host, port)

    @classmethod
    def get_instance(
        cls, host: str = "localhost", port: int = 8000
    ) -> "AgentInterface":
        """Get a singleton instance of AgentInterface."""
        if cls._instance is None:
            env_host = os.environ.get("JIVAS_HOST", "localhost")
            env_port = int(os.environ.get("JIVAS_PORT", "8000"))
            host = host or env_host
            port = port or env_port
            cls._instance = cls(host, port)
        return cls._instance

    async def init_agents(self) -> None:
        """Initialize agents - async compatible"""
        try:
            if not await self._jac.spawn_walker_async(
                walker_name="init_agents",
                module_name="jivas.agent.core.init_agents",
                attributes={"reporting": False},
            ):
                self.logger.error("Agent initialization failed")
        except Exception as e:
            self._jac.reset()
            self.logger.error(f"Init error: {e}\n{traceback.format_exc()}")

    async def webhook_exec(
        self,
        agent_id: str,
        key: str,
        namespace: str,
        action: str,
        walker: str,
        request: Request,
    ) -> JSONResponse:
        """Trigger webhook execution - async compatible"""
        try:

            if not self._jac.is_valid():
                self.logger.warning(
                    "Invalid API state for webhook, attempting to reinstate it..."
                )
                self._jac._authenticate()

            header = dict(request.headers)
            try:
                payload = await request.json()
                if not payload:
                    payload = {}
            except Exception:
                payload = {}

            walker_obj = await self._jac.spawn_walker_async(
                walker_name=walker,
                module_name=f"actions.{namespace}.{action}.{walker}",
                attributes={
                    "agent_id": agent_id,
                    "key": key,
                    "header": header,
                    "payload": payload,
                },
            )
            if not walker_obj:
                self.logger.error("Webhook execution failed")
                return JSONResponse(
                    content={"error": "Webhook execution failed"}, status_code=500
                )

            result = walker_obj.response
            return JSONResponse(
                status_code=result.get("status", 200),
                content=result.get("message", "200 OK"),
            )

        except Exception as e:
            self._jac.reset()
            self.logger.error(f"Webhook callback error: {e}\n{traceback.format_exc()}")
            return JSONResponse(
                content={"error": "Internal server error"}, status_code=500
            )

    def api_pulse(self, action_label: str, agent_id: str) -> dict:
        """Synchronous pulse API call"""
        if not self._jac.is_valid():
            self.logger.warning(
                "Invalid API state for pulse, attempting to reinstate it..."
            )
            self._jac._authenticate()

        # Clean parameters
        action_label = action_label.replace("action_label=", "")
        agent_id = agent_id.replace("agent_id=", "")

        endpoint = f"http://{self._jac.host}:{self._jac.port}/walker/do_pulse"
        headers = {"Authorization": f"Bearer {self._jac.token}"}
        payload = {"action_label": action_label, "agent_id": agent_id}

        try:
            response = requests.post(
                endpoint, json=payload, headers=headers, timeout=self.timeout
            )
            if response.status_code == 200:
                return response.json().get("reports", {})
            if response.status_code == 401:
                self._jac.reset()
        except Exception as e:
            self._jac.reset()
            self.logger.error(f"Pulse error: {e}\n{traceback.format_exc()}")

        return {}

    async def _finalize_interaction(
        self, interaction_node: Any, full_text: str, total_tokens: int
    ) -> None:
        """Finalize interaction in background"""
        try:
            interaction_node.set_text_message(message=full_text)
            interaction_node.add_tokens(total_tokens)

            await self._jac.spawn_walker_async(
                walker_name="update_interaction",
                module_name="jivas.agent.memory.update_interaction",
                attributes={"interaction_data": interaction_node.export()},
            )
        except Exception as e:
            self.logger.error(f"Finalize error: {e}")


# Module-level functions
def do_pulse(action_label: str, agent_id: str) -> dict:
    """Execute pulse action synchronously"""
    return AgentInterface.get_instance().api_pulse(action_label, agent_id)
