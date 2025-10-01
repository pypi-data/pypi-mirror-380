# Arazzo Runner [Beta]

[![Discord](https://img.shields.io/badge/JOIN%20OUR%20DISCORD-COMMUNITY-7289DA?style=plastic&logo=discord&logoColor=white)](https://discord.gg/yrxmDZWMqB)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-3.0-40c463.svg)](https://github.com/jentic/arazzo-engine/blob/HEAD/CODE_OF_CONDUCT.md)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://github.com/jentic/arazzo-engine/blob/HEAD/LICENSE)
[![PyPI version](https://badge.fury.io/py/arazzo-runner.svg)](https://badge.fury.io/py/arazzo-runner)

The Arazzo Runner is a workflow execution engine that processes and executes API workflows defined in the Arazzo format and individual API calls defined in OpenAPI specifications.

## Usage

### Execute a Workflow
```python
from arazzo_runner import ArazzoRunner

runner = ArazzoRunner.from_arazzo_path("../../workflows/discord.com/workflows.arazzo.json")

result = runner.execute_workflow("workflowId", {"param1": "value1"})
```

### Display Authentication Options
```python
from arazzo_runner import ArazzoRunner

runner = ArazzoRunner.from_arazzo_path("../../workflows/discord.com/workflows.arazzo.json")

print(runner.get_env_mappings())
```

### Execute a Single OpenAPI Operation
```python
from arazzo_runner import ArazzoRunner
# Execute a single OpenAPI operation with an operationId
result = runner.execute_operation("operationId", {"param1": "value1"})

# Execute a single OpenAPI operation by path
result = runner.execute_operation("GET /users/@me/guilds", {"param1": "value1"})
```

### Create a Runner with a Custom Base Path
```python
# Create a runner instance with a custom base path for resolving OpenAPI file paths
runner_with_base_path = ArazzoRunner.from_arazzo_path(
    "./my/arazzo.yaml", 
    base_path="./my/source/description/base"
)
```

## Authentication

Credentials are resolved from environment variables defined by the Arazzo Runner based on the Arazzo or OpenAPI file. You can see the authentication options by using `runner.get_env_mappings` or the `show-env-mappings` command line tool defined below.

The Arazzo Runner supports various authentication methods defined in OpenAPI specifications:

- **API Key**: Header, Query, or Cookie API keys
- **OAuth2**: Some OAuth2 Flows (Client Credentials, Password)
- **HTTP**: Basic and Bearer Authentication

### Auth Methods Not Yet Supported
- **OAuth2**: Authorization Code, Implicit
- **OpenID**: OpenID Connect
- **Custom**: Custom Authentication Schemes

## Command Line Usage

Usage:
```sh
uvx arazzo-runner <command> [command-specific arguments] [global options]
```

**Commands:**

1.  **`show-env-mappings`**: Show environment variable mappings for authentication based on an Arazzo or OpenAPI file.
    ```sh
    uvx arazzo-runner show-env-mappings [arazzo_path | --openapi-path PATH]
    ```
    -   `arazzo_path`: Path to the Arazzo YAML file (use this OR --openapi-path).
    -   `--openapi-path PATH`: Path to the OpenAPI spec file (use this OR arazzo_path).
    *One of the path arguments is required.*

2.  **`execute-workflow`**: Execute a workflow defined in an Arazzo file.
    ```sh
    uvx arazzo-runner execute-workflow <arazzo_path> --workflow-id <workflow_id> [--inputs <json_string>]
    ```
    -   `arazzo_path`: *Required*. Path to the Arazzo YAML file containing the workflow.
    -   `--workflow-id WORKFLOW_ID`: *Required*. ID of the workflow to execute.
    -   `--inputs INPUTS`: Optional JSON string of workflow inputs (default: `{}`).

3.  **`execute-operation`**: Execute a single API operation directly from an OpenAPI specification (or an Arazzo file for context).
    ```sh
    uvx arazzo-runner execute-operation [--arazzo-path PATH | --openapi-path PATH] [--operation-id ID | --operation-path PATH_METHOD] [--inputs <json_string>]
    ```
    -   `--arazzo-path PATH`: Path to an Arazzo file (provides context, use this OR --openapi-path).
    -   `--openapi-path PATH`: Path to the OpenAPI spec file (use this OR --arazzo-path).
        *One of the path arguments is required.*
    -   `--operation-id ID`: The `operationId` from the OpenAPI spec (use this OR --operation-path).
    -   `--operation-path PATH_METHOD`: The HTTP method and path (e.g., 'GET /users/{id}') from the OpenAPI spec (use this OR --operation-id).
        *One of the operation identifiers is required.*
    -   `--inputs INPUTS`: Optional JSON string of operation inputs (parameters, request body) (default: `{}`).

4.  **`list-workflows`**: List all available workflows defined in an Arazzo file.
    ```sh
    uvx arazzo-runner list-workflows <arazzo_path>
    ```
    -   `arazzo_path`: *Required*. Path to the Arazzo YAML file.

5.  **`describe-workflow`**: Show details of a specific workflow, including its summary, inputs, steps, and outputs.
    ```sh
    uvx arazzo-runner describe-workflow <arazzo_path> --workflow-id <workflow_id>
    ```
    -   `arazzo_path`: *Required*. Path to the Arazzo YAML file containing the workflow.
    -   `--workflow-id WORKFLOW_ID`: *Required*. ID of the workflow to describe.

6.  **`generate-example`**: Generate an example CLI command to execute a specified workflow, including placeholder inputs.
    ```sh
    uvx arazzo-runner generate-example <arazzo_path> --workflow-id <workflow_id>
    ```
    -   `arazzo_path`: *Required*. Path to the Arazzo YAML file containing the workflow.
    -   `--workflow-id WORKFLOW_ID`: *Required*. ID of the workflow to generate an example for.


**Global Options:**
- `--log-level {DEBUG,INFO,WARNING,ERROR,CRITICAL}`: Set the logging level (default: INFO).


**Examples:**

```sh
# Show environment variable mappings using an Arazzo file
uvx arazzo-runner show-env-mappings ./tests/fixtures/discord/discord.arazzo.yaml

# Show environment variable mappings using an OpenAPI file
uvx arazzo-runner show-env-mappings --openapi-path ./tests/fixtures/discord/discord.openapi.json

# Execute a workflow
uvx arazzo-runner execute-workflow ./tests/fixtures/discord/discord.arazzo.yaml --workflow-id getUserInfoAndSendMessage --inputs '{"recipient_id": "1234567890", "message_content": "Hello!"}'

# Execute a specific operation using its operationId and an OpenAPI file
uvx arazzo-runner execute-operation --openapi-path ./tests/fixtures/discord/discord.openapi.json --operation-id list_my_guilds --inputs '{}'

# Execute a specific operation using its path/method and an Arazzo file (for context)
uvx arazzo-runner execute-operation --arazzo-path ./tests/fixtures/discord/discord.arazzo.yaml --operation-path 'GET /users/@me/guilds' --inputs '{}' --log-level DEBUG

# List all available workflows
uvx arazzo-runner list-workflows ./tests/fixtures/discord/discord.arazzo.yaml

# Describe a specific workflow
uvx arazzo-runner describe-workflow ./tests/fixtures/discord/discord.arazzo.yaml --workflow-id getUserInfoAndSendMessage

# Generate an example CLI command to execute a workflow
uvx arazzo-runner generate-example ./tests/fixtures/discord/discord.arazzo.yaml --workflow-id getUserInfoAndSendMessage
```

**Help:**
```sh
# General help
uvx arazzo-runner --help

# Help for a specific command (e.g., execute-operation)
uvx arazzo-runner execute-operation --help
```

## Server URL Configuration

Arazzo Runner supports dynamic server URLs as defined in the `servers` object of an OpenAPI specification. This allows you to define API server URLs with templated variables (e.g., `https://{instance_id}.api.example.com/v1` or `https://api.example.com/{region}/users`).

### Variable Resolution

When an operation requires a server URL with variables, Arazzo Runner resolves these variables in the following order of precedence:

1.  **Runtime Parameters**: Values passed explicitly when executing an operation or workflow (e.g., via the `--server-variables` CLI argument or the `runtime_params` parameter in `execute_operation`/`execute_workflow` methods). These parameters should be provided as a dictionary where keys match the expected environment variable names for the server variables (see below).
2.  **Environment Variables**: If not provided as a runtime parameter, Arazzo Runner attempts to find an environment variable.
3.  **Default Values**: If not found in runtime parameters or environment variables, the `default` value specified for the variable in the OpenAPI document's `servers` object is used.

If a variable in the URL template cannot be resolved through any of these means, and it does not have a default value, an error will occur.

### Environment Variable Naming

The environment variables for server URLs follow these naming conventions:

-   If the OpenAPI specification's `info.title` is available and an `API_TITLE_PREFIX` can be derived from it (typically the first word of the title, uppercased and sanitized, e.g., `PETSTORE` from "Petstore API"), the format is:
    `[API_TITLE_PREFIX_]RUNNER_SERVER_<VAR_NAME_UPPERCASE>`
    Example: `PETSTORE_RUNNER_SERVER_REGION=us-east-1`

-   If an `API_TITLE_PREFIX` cannot be derived (e.g., `info.title` is missing or empty), the format is:
    `RUNNER_SERVER_<VAR_NAME_UPPERCASE>`
    Example: `RUNNER_SERVER_INSTANCE_ID=my-instance-123`

The `<VAR_NAME_UPPERCASE>` corresponds to the variable name defined in the `servers` object's `variables` map (e.g., `region` or `instance_id`), converted to uppercase.

You can use the `show-env-mappings` CLI command to see the expected environment variable names for server URLs, alongside authentication variables, for a given OpenAPI specification.

### Example

Consider an OpenAPI specification with:
- `info.title: "My Custom API"`
- A server definition:
  ```yaml
  servers:
    - url: "https://{instance}.api.example.com/{version}"
      variables:
        instance:
          default: "prod"
          description: "The API instance name."
        version:
          default: "v1"
          description: "API version."
  ```

To set the `instance` to "dev" and `version` to "v2" via environment variables, you would set:
```sh
export MYCUSTOM_RUNNER_SERVER_INSTANCE=dev
export MYCUSTOM_RUNNER_SERVER_VERSION=v2
```
(Assuming "MYCUSTOM" is derived from "My Custom API").

Alternatively, to provide these at runtime via the CLI when executing an operation:
```sh
uvx arazzo-runner execute-operation --openapi-path path/to/spec.yaml --operation-id someOperation \
  --server-variables '{"MYCUSTOM_RUNNER_SERVER_INSTANCE": "staging", "MYCUSTOM_RUNNER_SERVER_VERSION": "v2beta"}'
```

### Blob Storage

Arazzo Runner supports blob storage for handling large binary responses without putting the raw binary into LLM context windows. This feature is **disabled by default** and must be explicitly enabled.

#### Enabling Blob Storage

Instantiate either `LocalFileBlobStore` (persists to disk) or `InMemoryBlobStore` (ephemeral) and pass it to `ArazzoRunner`:

```python
from arazzo_runner import ArazzoRunner, LocalFileBlobStore

blob_store = LocalFileBlobStore()  # Or InMemoryBlobStore() for testing

runner = ArazzoRunner.from_arazzo_path("workflow.yaml", blob_store=blob_store)
result = runner.execute_workflow("download-file", {"url": "https://example.com/large-file.pdf"})
```

Blob storage is **disabled** when `blob_store` is omitted or `None` (the default).

### Configuration

You can configure the blob storage threshold and directory via environment variables:
- `ARAZZO_BLOB_THRESHOLD`: Size threshold in bytes for storing as blob (default: 32768)
- `BLOB_STORE_PATH`: Directory for blob storage (default: ./blobs)

**State Management**: Blob storage introduces additional state that must be managed:
- Blob files are stored on disk and referenced by unique IDs
- State persists between workflow executions

## Development

All following sections assume that you're inside the `./runner` directory of the `arazzo-engine` monorepo.

### Prerequisites

Python 3.11 or higher is required. You can check your Python version with:

```bash
python --version
```

### Installation

1. Install PDM if you haven't already:
   ```bash
   # Install PDM
   curl -sSL https://pdm.fming.dev/install-pdm.py | python3 -
   
   # Or with Homebrew (macOS/Linux)
   brew install pdm
   
   # Or with pip
   pip install pdm
   ```

2. Install project dependencies:
   ```bash
   # Install dependencies
   pdm install
   ```

### Executing Runner CLI commands

You can run the Arazzo Runner CLI commands using python's `-m` flag:

```bash
python -m arazzo_runner --help
```

This will display the help message for the Arazzo Runner CLI with all available commands.

### Running Tests

The Arazzo Runner includes a comprehensive testing framework for workflow validation:

- Automated test fixtures for different workflow scenarios
- Mock HTTP responses based on OpenAPI specs
- Custom mock responses for specific endpoints
- Validation of workflow outputs and API call counts

For details on testing, see [Arazzo Runner Testing Framework](https://github.com/jentic/arazzo-engine/blob/main/runner/tests/README.md)

```bash
# Run all tests
pdm run test

# Run making actual API calls
pdm run test-real 

# Run a specific test file
pdm run test tests/test_arazzo_runner.py
```

### Code Formatting & Linting

The project uses [black](https://github.com/psf/black), [isort](https://github.com/PyCQA/isort) and [ruff](https://docs.astral.sh/ruff/) for code formatting.

```bash
# Check formatting & linting without making changes
pdm run lint

# Format & lint code 
pdm run lint:fix
```

#### Available PDM Scripts

- `pdm run test` - Run all tests
- `pdm run test` - Run all tests making actual API calls
- `pdm run lint` - Check formatting & linting without making changes
- `pdm run lint:fix` - Format & lint code

## Overview

Arazzo Runner orchestrates API workflows by:

- Loading and validating Arazzo workflow documents
- Executing workflow steps sequentially or conditionally
- Evaluating runtime expressions and success criteria
- Extracting and transforming data between steps
- Handling flow control (continue, goto, retry, end)
- Supporting nested workflow execution
- Providing event callbacks for workflow lifecycle events
- Managing authentication requirements across different APIs

## Arazzo Format

The Arazzo specification is our workflow definition format that orchestrates API calls using OpenAPI specifications.

- Schema: [arazzo-schema.yaml](https://github.com/jentic/arazzo-engine/blob/main/runner/arazzo_spec/arazzo-schema.yaml)
- Documentation: [arazzo-spec.md](https://github.com/jentic/arazzo-engine/blob/main/runner/arazzo_spec/arazzo-spec.md)
