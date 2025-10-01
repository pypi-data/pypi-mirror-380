# `trustyai-ragas` <br> Ragas as an Out-of-Tree Llama Stack Provider

[![PyPI version](https://img.shields.io/pypi/v/llama_stack_provider_ragas.svg)](https://pypi.org/project/llama-stack-provider-ragas/)

⚠️ Warning! This project is in early stages of development!

## About
This repository implements [Ragas](https://github.com/explodinggradients/ragas) as an out-of-tree [Llama Stack](https://github.com/meta-llama/llama-stack) evaluation provider.

## Features
The goal is to provide all of Ragas' evaluation functionality over Llama Stack's eval API, while leveraging the Llama Stack's built-in APIs for inference (llms and embeddings), datasets, and benchmarks.

There are two versions of the provider:
- `inline`: runs the Ragas evaluation in the same process as the Llama Stack server.
- `remote`: runs the Ragas evaluation in a remote process, using Kubeflow Pipelines.

## Prerequisites
- Python 3.12
- [uv](https://docs.astral.sh/uv/)
- The remote provider requires a running [Kubeflow Pipelines](https://www.kubeflow.org/docs/components/pipelines) server.

## Setup
- Clone this repository
    ```bash
    git clone <repository-url>
    cd llama-stack-provider-ragas
    ```

- Create and activate a virtual environment
    ```bash
    uv venv
    source .venv/bin/activate
    ```

- Install (optionally as an editable package). There's `distro`, `remote` and `dev` optional dependencies to run the sample LS distribution and the KFP-enabled remote provider. Installing the `dev` dependencies will also install the `distro` and `remote` dependencies.
    ```bash
    uv pip install -e ".[dev]"
    ```
- The sample LS distributions (one for inline and one for remote provider) is a simple LS distribution that uses Ollama for inference and embeddings. See the provider-specific sections below for setup and run commands.

### Inline provider

Create a `.env` file with the required environment variable:
```bash
EMBEDDING_MODEL=all-MiniLM-L6-v2
```

Run the server:
```bash
dotenv run uv run llama stack run distribution/run-inline.yaml
```

### Remote provider

Create a `.env` file with the following:
```bash
# Required for both inline and remote
EMBEDDING_MODEL=all-MiniLM-L6-v2

# Required for remote provider
KUBEFLOW_LLAMA_STACK_URL=<your-llama-stack-url>
KUBEFLOW_PIPELINES_ENDPOINT=<your-kfp-endpoint>
KUBEFLOW_NAMESPACE=<your-namespace>
KUBEFLOW_BASE_IMAGE=quay.io/diegosquayorg/my-ragas-provider-image:latest
```

Where:
- `KUBEFLOW_LLAMA_STACK_URL`: The URL of the llama stack server that the remote provider will use to run the evaluation (LLM generations and embeddings, etc.). If you are running Llama Stack locally, you can use [ngrok](https://ngrok.com/) to expose it to the remote provider.
- `KUBEFLOW_PIPELINES_ENDPOINT`: You can get this via `kubectl get routes -A | grep -i pipeline` on your Kubernetes cluster.
- `KUBEFLOW_NAMESPACE`: The name of the data science project where the Kubeflow Pipelines server is running.
- `KUBEFLOW_BASE_IMAGE`: The image used to run the Ragas evaluation in the remote provider. See `Containerfile` for details. There is a public version of this image at `quay.io/diegosquayorg/my-ragas-provider-image:latest`.

Run the server:
```bash
dotenv run uv run llama stack run distribution/run-remote.yaml
```


## Usage
See the demos in the `demos` directory.
