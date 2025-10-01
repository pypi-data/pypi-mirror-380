from __future__ import annotations

import argparse
import asyncio
import json
import logging
import os
import signal
import uuid
from contextlib import asynccontextmanager, suppress
from typing import Dict, List, Tuple

import uvicorn
from fastmcp import FastMCP
from starlette.applications import Starlette
from starlette.responses import Response
from starlette.routing import Mount, Route

from mcp_jupyter_notebook.tools.notebook import register_notebook_tools
from mcp_jupyter_notebook.tools.postgresql import register_postgresql_tools

from jupyter_agent_toolkit.notebook import NotebookSession
from jupyter_agent_toolkit.utils import create_kernel, create_notebook_transport


# ───────────────────────── logging ─────────────────────────

def _init_logging() -> logging.Logger:
    """
    Initialize logging from env (MCP_JUPYTER_NOTEBOOK_LOG_LEVEL).
    Defaults to INFO if unset/invalid.
    """
    level = getattr(
        logging,
        os.getenv("MCP_JUPYTER_NOTEBOOK_LOG_LEVEL", "INFO").upper(),
        logging.INFO,
    )
    logging.basicConfig(
        level=level, format="%(asctime)s %(levelname)s %(name)s: %(message)s"
    )
    return logging.getLogger("mcp-jupyter")


log = _init_logging()


# ───────────────── env helpers & header parsing ─────────────────

def _env_bool(name: str, default: bool = False) -> bool:
    """
    Parse a boolean-like env var. Accepts: 1/0, true/false, yes/no (case-insensitive).
    """
    raw = os.getenv(name)
    if raw is None:
        return default
    val = raw.strip().lower()
    if val in {"1", "true", "t", "yes", "y", "on"}:
        return True
    if val in {"0", "false", "f", "no", "n", "off"}:
        return False
    log.warning("Unrecognized boolean for %s=%r; using default=%s", name, raw, default)
    return default


def _env_str(name: str, default: str | None = None) -> str | None:
    """
    Get a string env var with trimming; returns default if empty/whitespace.
    """
    raw = os.getenv(name)
    if raw is None:
        return default
    s = raw.strip()
    return s if s else default


def _parse_headers_env(var: str = "MCP_JUPYTER_HEADERS_JSON") -> Dict[str, str]:
    """
    Optional extra headers (Cookie/XSRF) as a JSON object.
    Non-dict or invalid JSON are ignored with a warning.
    """
    raw = os.getenv(var)
    if not raw:
        return {}
    try:
        h = json.loads(raw)
        if not isinstance(h, dict):
            raise ValueError("headers JSON must be an object")
        # ensure str->str
        return {str(k): str(v) for k, v in h.items()}
    except Exception as e:
        log.warning("Ignoring invalid %s (not JSON object): %s", var, e)
        return {}


def _parse_toolsets(cli_value: str | None = None) -> List[str]:
    """
    Return a normalized list of toolsets to register.
    NOTE: 'notebook' is ALWAYS included (cannot be removed via CLI/ENV).
    Supported extras: 'postgresql' (more can be added later).
    """
    raw = (cli_value or os.getenv("MCP_JUPYTER_TOOLSETS", "")).strip()
    extras: List[str] = []
    if raw:
        parts = [p.strip().lower() for p in raw.split(",") if p.strip()]
        # Expand 'all' to known toolsets (excluding 'notebook' which is implicit)
        for p in parts:
            if p == "all":
                extras.extend(["postgresql"])
            elif p in {"postgresql"}:
                extras.append(p)
            else:
                log.warning("Unknown toolset '%s' ignored.", p)

    # Always include notebook first, then unique extras in order
    out, seen = ["notebook"], set(["notebook"])
    for p in extras:
        if p not in seen:
            out.append(p)
            seen.add(p)
    return out


# ──────────────── session construction ────────────────

def _make_session_from_env() -> NotebookSession:
    """
    Build a NotebookSession from env in modern toolkit style.

    Modes:
      - server (remote Jupyter): remote kernel + collab transport (prefer_collab=True)
      - local: local kernel + local transport (prefer_collab=False)
    """
    mode = _env_str("MCP_JUPYTER_SESSION_MODE", "server") or "server"
    mode = mode.lower()
    kernel_name = _env_str("MCP_JUPYTER_KERNEL_NAME", "python3") or "python3"
    notebook_path = _env_str("MCP_JUPYTER_NOTEBOOK_PATH") or f"mcp_{uuid.uuid4().hex[:8]}.ipynb"

    if mode == "server":
        base_url = _env_str("MCP_JUPYTER_BASE_URL")
        if not base_url:
            raise RuntimeError("MCP_JUPYTER_BASE_URL is required in server mode")
        token = _env_str("MCP_JUPYTER_TOKEN")  # may be None
        headers = _parse_headers_env()

        # Collab ON (non-negotiable for remote)
        prefer_collab = True

        log.info(
            "Creating remote NotebookSession mode=%s kernel=%s nb=%s base_url=%s collab=%s headers=%s",
            mode, kernel_name, notebook_path, base_url, prefer_collab, bool(headers),
        )

        kernel = create_kernel(
            "remote",
            base_url=base_url,
            token=token,
            headers=headers or None,
            kernel_name=kernel_name,
        )
        doc = create_notebook_transport(
            "remote",
            notebook_path,
            base_url=base_url,
            token=token,
            headers=headers or None,
            prefer_collab=prefer_collab,
            create_if_missing=True,
        )
        return NotebookSession(kernel=kernel, doc=doc)

    # local mode
    log.info("Creating local NotebookSession mode=%s kernel=%s nb=%s", mode, kernel_name, notebook_path)
    kernel = create_kernel("local", kernel_name=kernel_name)
    doc = create_notebook_transport(
        "local",
        notebook_path,
        prefer_collab=False,
        create_if_missing=True,
    )
    return NotebookSession(kernel=kernel, doc=doc)


# ───────────────────── MCP server core ─────────────────────

def _register_toolsets(server: FastMCP, session: NotebookSession, toolsets: List[str]) -> None:
    """Register tools according to selected toolsets. 'notebook' is always included."""
    register_notebook_tools(server, session)
    if "postgresql" in toolsets:
        register_postgresql_tools(server, session)


def get_server_and_session(toolsets: List[str]) -> Tuple[FastMCP, NotebookSession]:
    """Create the FastMCP server and NotebookSession, and register tools."""
    server = FastMCP("mcp-jupyter")
    session: NotebookSession = _make_session_from_env()
    _register_toolsets(server, session, toolsets)
    log.info("Toolsets registered: %s", ", ".join(toolsets))
    return server, session


async def _graceful_stop(session: NotebookSession | None = None) -> None:
    """Close collab websocket, kernel, and underlying clients safely."""
    try:
        if session:
            await session.stop()
            log.info("NotebookSession stopped.")
    except Exception as e:
        log.warning("Error during shutdown: %s", e)


def _run_coro_safely(coro) -> None:
    """
    Run/await a coroutine without conflicting with an existing event loop.
    - If no loop is running, uses asyncio.run().
    - If a loop is running (e.g., under uvicorn), schedules a task on it.
    """
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        asyncio.run(coro)
        return
    loop.create_task(coro)


# ─────────────────────── stdio transport ───────────────────────

def run_stdio(tools_arg: str | None = None) -> None:
    log.info("Starting MCP in stdio mode.")
    toolsets = _parse_toolsets(tools_arg)
    server, session = get_server_and_session(toolsets)

    # Optional: best-effort signal logging on Unix (no loop control here)
    with suppress(Exception):
        loop = asyncio.get_event_loop()
        for sig in (signal.SIGINT, signal.SIGTERM):
            with suppress(NotImplementedError):
                loop.add_signal_handler(sig, lambda s=sig: log.info("Received signal %s", s))

    try:
        server.run("stdio")  # blocking until EOF / Ctrl-C
    except KeyboardInterrupt:
        log.info("Interrupted by user.")
    finally:
        _run_coro_safely(_graceful_stop(session))


# ─────────────────────── SSE transport ───────────────────────

def run_sse(host: str = "127.0.0.1", port: int = 8000, tools_arg: str | None = None) -> None:
    """
    SSE endpoint at /sse and POST message endpoint mounted by SseServerTransport.
    """
    log.info("Starting MCP in SSE mode on http://%s:%d", host, port)
    from mcp.server.sse import SseServerTransport  # lazy import

    toolsets = _parse_toolsets(tools_arg)
    server, session = get_server_and_session(toolsets)
    sse = SseServerTransport("/messages/")

    async def handle_sse(request):
        log.info("🔌 SSE connection established")
        async with sse.connect_sse(request.scope, request.receive, request._send) as (read_stream, write_stream):
            await server._mcp_server.run(
                read_stream,
                write_stream,
                server._mcp_server.create_initialization_options(),
            )
        return Response(status_code=200)

    app = Starlette(
        debug=False,
        routes=[
            Route("/sse", endpoint=handle_sse),
            Mount("/messages/", app=sse.handle_post_message),
        ],
    )

    try:
        uvicorn.run(app, host=host, port=port, log_level="info")
    finally:
        _run_coro_safely(_graceful_stop(session))


# ─────────────── streamable HTTP transport ───────────────

def run_streamable_http(
    host: str = "127.0.0.1",
    port: int = 8000,
    *,
    stateless: bool = False,
    json_response: bool = False,
    tools_arg: str | None = None,
) -> None:
    """
    Streamable HTTP transport at /mcp.
    - stateless: each request is isolated (no server-side session state)
    - json_response: return JSON envelopes instead of SSE
    """
    log.info(
        "Starting MCP in streamable HTTP mode at http://%s:%d (stateless=%s json_response=%s)",
        host, port, stateless, json_response,
    )
    from mcp.server.streamable_http_manager import StreamableHTTPSessionManager  # lazy import

    toolsets = _parse_toolsets(tools_arg)
    server, session = get_server_and_session(toolsets)
    mgr = StreamableHTTPSessionManager(
        server._mcp_server,
        event_store=None,
        json_response=json_response,
        stateless=stateless,
    )

    async def handle_streamable_http(scope, receive, send):
        log.info("🔌 Streamable HTTP request")
        await mgr.handle_request(scope, receive, send)

    app = Starlette(
        debug=False,
        routes=[Mount("/mcp", app=handle_streamable_http)],
    )

    @asynccontextmanager
    async def _lifespan():
        async with mgr.run():
            try:
                yield
            finally:
                await _graceful_stop(session)

    async def _serve():
        async with _lifespan():
            config = uvicorn.Config(app, host=host, port=port, log_level="info")
            srv = uvicorn.Server(config)
            await srv.serve()

    asyncio.run(_serve())


# ───────────────────────── CLI & entry ─────────────────────────

def _parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Run the MCP Jupyter server.")
    p.add_argument("--transport", choices=["stdio", "sse", "streamable-http"], default="stdio")

    p.add_argument("--host", default=os.getenv("MCP_HTTP_HOST", "127.0.0.1"))
    p.add_argument("--port", type=int, default=int(os.getenv("MCP_HTTP_PORT", "8000")))
    p.add_argument(
        "--stateless",
        action="store_true",
        default=False,
        help="Streamable HTTP: stateless mode",
    )
    p.add_argument(
        "--json-response",
        action="store_true",
        default=False,
        help="Streamable HTTP: JSON envelopes",
    )
    p.add_argument(
        "--tools",
        default=os.getenv("MCP_JUPYTER_TOOLSETS", ""),
        help="Comma-separated toolsets to add (notebook is always included). "
             "Supported: 'postgresql', or 'all'. Example: --tools postgresql",
    )
    return p.parse_args()


def main() -> None:
    """
    Entry point. Logs a brief, non-sensitive startup summary.
    """
    mode = os.getenv("MCP_JUPYTER_SESSION_MODE", "server")
    kernel = os.getenv("MCP_JUPYTER_KERNEL_NAME", "python3")
    nb = os.getenv("MCP_JUPYTER_NOTEBOOK_PATH", "<auto>")
    toolsets_raw = os.getenv("MCP_JUPYTER_TOOLSETS", "")
    log.info("mcp-jupyter launching… mode=%s kernel=%s notebook=%s toolsets=%s",
             mode, kernel, nb, toolsets_raw or "(default: notebook)")

    args = _parse_args()

    # notebook tools are always included; args.tools only adds extras
    if args.transport == "stdio":
        run_stdio(args.tools)
    elif args.transport == "sse":
        run_sse(host=args.host, port=args.port, tools_arg=args.tools)
    elif args.transport == "streamable-http":
        run_streamable_http(
            host=args.host,
            port=args.port,
            stateless=args.stateless,
            json_response=args.json_response,
            tools_arg=args.tools,
        )
    else:
        raise SystemExit(f"Unknown transport: {args.transport}")


if __name__ == "__main__":
    main()