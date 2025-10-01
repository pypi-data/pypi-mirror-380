# JIVAS Web Server (jvserve)

![GitHub release (latest by date)](https://img.shields.io/github/v/release/TrueSelph/jvserve)
![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/TrueSelph/jvserve/test-jvserve.yaml)
![GitHub issues](https://img.shields.io/github/issues/TrueSelph/jvserve)
![GitHub pull requests](https://img.shields.io/github/issues-pr/TrueSelph/jvserve)
![GitHub](https://img.shields.io/github/license/TrueSelph/jvserve)

`jvserve` is a FastAPI-based web server designed for loading and interacting with JIVAS agents. It is built on top of [`jac-cloud`](https://github.com/Jaseci-Labs/jaseci/tree/main/jac-cloud) and provides a robust platform for managing jivas agent jobs, handling webhooks, and executing actions within the JIVAS ecosystem.

## Installation

To install `jvserve`, use `pip`:

```sh
pip install jvserve
```

## Usage

To use `jvserve`, you can start the server with the following command:

```sh
jac jvserve <path_to_your_jac_file>
```

For example:

```sh
jac jvserve main.jac
```

You can also start a file server to serve static files:

```sh
jac jvfileserve <directory>
```

For example:

```sh
jac jvfileserve ./static
```

### Supported Arguments

- **filename**: Path to your JAC file.
- **host**: Host address to bind the server (default: `localhost`).
- **port**: Port number to bind the server (default: `8000`).
- **loglevel**: Logging level (default: `INFO`).
- **workers**: Number of worker processes (optional).

Example with all arguments:

```sh
jac jvserve main.jac --host 127.0.0.1 --port 8080 --loglevel DEBUG --workers 4
```

## API Endpoints

- **Interact with Agent**: `/interact` (POST)
- **Execute Webhook**: `/webhook/{key}` (GET, POST)
- **Execute Action Walker**: `/action/walker` (POST)

You can see all endpoints at the URL `/docs`.

## 🔰 Contributing

- **🐛 [Report Issues](https://github.com/TrueSelph/jvserve/issues)**: Submit bugs found or log feature requests for the `jvserve` project.
- **💡 [Submit Pull Requests](https://github.com/TrueSelph/jvserve/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your GitHub account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/TrueSelph/jvserve
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to GitHub**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details open>
<summary>Contributor Graph</summary>
<br>
<p align="left">
    <a href="https://github.com/TrueSelph/jvserve/graphs/contributors">
        <img src="https://contrib.rocks/image?repo=TrueSelph/jvserve" />
   </a>
</p>
</details>

## 🎗 License

This project is protected under the Apache License 2.0. See [LICENSE](./LICENSE) for more information.

## Additional Information

Since `jvserve` is a wrapper around `jac-cloud`, it supports all the primitives available in `jac-cloud`. You can find more information about `jac-cloud` primitives [here](https://www.jac-lang.org/for_coders/jac-cloud/jac_cloud/).
