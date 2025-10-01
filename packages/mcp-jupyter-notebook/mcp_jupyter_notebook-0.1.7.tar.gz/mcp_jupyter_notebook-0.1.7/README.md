# MCP Jupyter Notebook Server

A Model Context Protocol (MCP) server that lets AI agents drive a live Jupyter notebook session adding code/markdown, managing packages, and exploring connected data sources.

---

## Overview

This server exposes a single Jupyter notebook session over MCP. Agents can create and run cells, install packages, and (via optional data-source helpers) fetch tabular data into dataframes for analysis and visualization.

---

## Tools

The server organizes its capabilities into **Notebook** (core notebook interaction) and **Data Explorers** (structured ways to pull external data into dataframes).

### Notebook

Core interactions with the Jupyter session.

| Tool | What it does |
|---|---|
| `notebook.markdown.add` | Append a markdown cell and return the inserted cell’s index. |
| `notebook.code.run` | Append a Python code cell, execute it, and return rich outputs (stdout/stderr/rendered display). |
| `notebook.packages.add` | Ensure one or more Python packages are installed/available in the kernel. |

---

### Data Explorers

Data Explorer tools provide a consistent workflow for bringing external datasets into the notebook environment:

1. **Bootstrap**: ensure a client/driver exists in the kernel (e.g., Postgres client).  
2. **Visible cell**: insert a cell that materializes a pandas DataFrame (`df_<id>`) and shows a small preview.  
3. **Hidden metadata**: return compact JSON (schema, row/col counts, sample rows) to guide further exploration.  

---

#### PostgreSQL

**Purpose:** explore a Postgres database directly from the notebook session.

**Environment:** requires a DSN in one of:
- `PG_DSN`, `POSTGRES_DSN`, or `DATABASE_URL`

**Tools**

| Tool | What it does |
|---|---|
| `db.postgresql.query.to_df` | Runs a SQL query (with optional `limit`), assigns the result to a notebook variable `df_<id>`, shows `df_<id>.head(5)` in the notebook, and returns metadata (schema, row/col counts, and a sample). |
| `db.postgresql.schema.list_tables` | Lists base tables/views for a schema (or all schemas). Can include materialized views if requested. |
| `db.postgresql.schema.list_columns` | Returns column definitions (name, type, nullability, defaults) for a given `(schema, table)`. |
| `db.postgresql.schema.tree` | Returns a compact `{schema, tables:[...]}` mapping (optionally limited per schema), excluding system schemas for clarity. |

**Design notes**
- Uses a single shared Postgres client (`__JAT_PG__`) per kernel for efficiency.  
- Visible query cells always materialize a DataFrame with a deterministic notebook variable name (`df_<id>`).  
- Hidden execution captures metadata as JSON, tolerant of ANSI escape codes and errors.

## Installation

### With pip

```sh
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
```

### With uv

```sh
uv venv .venv
source .venv/bin/activate
uv pip install -e '.[dev]'
```

---

## Usage

### 1. Select Jupyter Connection Mode (Environment Variables)

Set these environment variables to control how the server connects to Jupyter:

- **MCP_JUPYTER_SESSION_MODE**: `server` (remote Jupyter, default) or `local` (local kernel)
- **MCP_JUPYTER_BASE_URL**: Jupyter server URL (required in `server` mode, e.g., `http://localhost:8888`)
- **MCP_JUPYTER_TOKEN**: Jupyter API token (required in `server` mode)
- **MCP_JUPYTER_KERNEL_NAME**: Kernel name (default: `python3`)
- **MCP_JUPYTER_NOTEBOOK_PATH**: Notebook file path (default: random, e.g., `mcp_<id>.ipynb`)
- **MCP_JUPYTER_NOTEBOOK_LOG_LEVEL**: Log level (default: `INFO`)

**Example:**
```sh
export MCP_JUPYTER_SESSION_MODE=server
export MCP_JUPYTER_BASE_URL=http://localhost:8888
export MCP_JUPYTER_TOKEN=ceb03195-18f5-4138-a24c-5bab7fecb97d
export MCP_JUPYTER_KERNEL_NAME=python3
export MCP_JUPYTER_NOTEBOOK_PATH=mcp_example.ipynb
```

### 2. Select Transport Mode (CLI Argument)

Choose how the MCP server exposes itself to clients:

- **stdio** (default): For local/desktop agent integration (recommended for most MCP clients)
- **sse**: For legacy web/SSE clients
- **streamable-http**: For HTTP API integration

Specify the transport with the `--transport` CLI argument:

```sh
mcp-jupyter-notebook --transport stdio           # (default, for local/desktop)
mcp-jupyter-notebook --transport sse             # (for legacy web/SSE)
mcp-jupyter-notebook --transport streamable-http # (for HTTP API)
```

You can also set host/port for HTTP/SSE modes:

```sh
mcp-jupyter-notebook --transport streamable-http --host 0.0.0.0 --port 8000
```

> **Note:**
> When running the MCP server with `uv` in stdio mode (the default transport), Ctrl+C may not always stop the server due to how `uv` manages process signals and stdio. Use Ctrl+D (EOF) or kill the process from another terminal if needed. For local development, running with `python -m mcp_jupyter_notebook.server` allows Ctrl+C to work as expected.

---

### 3. Launch the Server

After installation, you can launch the MCP Jupyter Notebook server from anywhere using the CLI entrypoint or as a Python module:

```sh
mcp-jupyter-notebook [--transport ...]
```

Or with uv:

```sh
uv run mcp-jupyter-notebook [--transport ...]
```

Or run directly as a module:

```sh
python -m mcp_jupyter_notebook.server [--transport ...]
```

---

### 4. Example MCP Client Configuration

To use with an MCP client (e.g., Claude Desktop, VS Code, etc.):

```json
{
    "mcpServers": {
        "jupyter": {
            "command": "uvx",
            "args": [ "mcp-jupyter-notebook", "--transport", "stdio"  ],
            "env": {
                "MCP_JUPYTER_SESSION_MODE": "server",
                "MCP_JUPYTER_BASE_URL": "http://localhost:8888",
                "MCP_JUPYTER_TOKEN": "<your-jupyter-token>",
                "MCP_JUPYTER_KERNEL_NAME": "python3",
                "MCP_JUPYTER_NOTEBOOK_PATH": "mcp_<id>.ipynb"
            }
        }
    }
}
```

**Note:** Do not reference a script path. Use the CLI entrypoint (`mcp-jupyter-notebook`) after installing the package.

---

## Release Process

To publish a new release to PyPI:

0. Install dev dependencies
    ```sh
    uv pip install -e ".[dev]"
    ``` 
1. Ensure all changes are committed and tests pass:
    ```sh
    uv run pytest tests/
    ```
2. Create and push an **annotated tag** for the release:
    ```sh
    git tag -a v0.1.0 -m "Release 0.1.0"
    git push origin v0.1.0
    ```
3. Checkout the tag to ensure you are building exactly from it:
    ```sh
    git checkout v0.1.0
    ```
4. Clean old build artifacts:
    ```sh
    rm -rf dist
    rm -rf build
    rm -rf src/*.egg-info
    ```
5. Upgrade build and upload tools:
    ```sh
    uv pip install --upgrade build twine packaging setuptools wheel setuptools_scm
    ```
6. Build the package:
    ```sh
    uv run python -m build
    ```
7. (Optional) Check metadata:
    ```sh
    uv run twine check dist/*
    ```
8. Upload to PyPI:
    ```sh
    uv run twine upload dist/*
    ```

**Notes:**
* Twine ≥ 6 and packaging ≥ 24.2 are required for modern metadata support.
* Always build from the tag (`git checkout vX.Y.Z`) so setuptools_scm resolves the exact version.
* `git checkout v0.1.0` puts you in detached HEAD mode; that’s normal. When done, return to your branch with:
    ```sh
    git switch -
    ```
* If you’re building in CI, make sure tags are fetched:
    ```sh
    git fetch --tags --force --prune
    git fetch --unshallow || true
    ```

---