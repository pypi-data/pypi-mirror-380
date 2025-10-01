from __future__ import annotations

import json
import re
import uuid
from typing import Any, Dict, Optional

from jupyter_agent_toolkit.notebook import NotebookSession
from jupyter_agent_toolkit.utils.execution import (
    execute_code,
    invoke_code_cell,
)
from jupyter_agent_toolkit.utils.packages import update_dependencies
from mcp.server import Server
from pydantic import Field

_ANSI_RE = re.compile(r"\x1B\[[0-?]*[ -/]*[@-~]")

# Single shared Postgres client per kernel
_PG_VAR = "__JAT_PG__"


def register_postgresql_tools(server: Server, session: NotebookSession) -> None:
    """
    Register PostgreSQL tools.

    Tools
    -----
    db.postgresql.query.to_df(raw_sql: str, *, limit: Optional[int] = 50) -> dict
        • Ensures deps and a shared Postgres client (__JAT_PG__) exist in the kernel.
        • Inserts ONE visible code cell:
            - runs `pg.query_df(sql=_sql, limit=limit)`,
            - assigns the result to a unique notebook var `df_<id>`,
            - leaves `df_<id>.head(5)` as the last expression so Jupyter renders a preview.
        • Then runs hidden code to read `df_<id>` and return metadata:
            schema (dtypes), row_count, col_count, and a small sample (head).

    db.postgresql.schema.list_tables(schema_name: Optional[str] = None, include_matviews: bool = False)
        • Hidden only. Returns base tables/views (and optionally materialized views).

    db.postgresql.schema.list_columns(schema_name: str, table: str)
        • Hidden only. Returns information_schema column metadata.

    db.postgresql.schema.tree(limit_per_schema: Optional[int] = 100)
        • Hidden only. Returns [{schema, tables:[...]}], limited per schema.

    Notes
    -----
    - DSN must be set in PG_DSN / POSTGRES_DSN / DATABASE_URL.
    - LIMIT is applied client-side via query_df(..., limit=...); pass None to disable.
    """

    # ---------- shared helpers ----------

    async def _ensure_started():
        if not await session.is_connected():
            await session.start()

    async def _ensure_deps_once() -> bool:
        """Best-effort dependency ensure; OK if already present."""
        return await update_dependencies(
            session.kernel,
            [
                "psycopg[binary]>=3.1",
                "pandas>=2.2",
                "pyarrow>=16.0",
                "jupyter-agent-toolkit",
            ],
        )

    async def _run_hidden(code: str, *, timeout: float = 60.0) -> Dict[str, Any]:
        """
        Execute hidden Python in the kernel that prints exactly one JSON line.
        Parse and return that JSON; if execution fails or JSON isn't present on stdout,
        fall back to stream outputs and surface kernel diagnostics.
        """
        res = await execute_code(session.kernel, code, timeout=timeout, format_outputs=True)

        if res.status != "ok":
            return {
                "ok": False,
                "error": res.error_message or (res.stderr or "Kernel execution error"),
                "stderr": res.stderr,
                "stdout": res.stdout,
                "outputs": res.text_outputs,
            }

        raw = (res.stdout or "").strip()
        if not raw:
            raw = ("\n".join(res.text_outputs) if res.text_outputs else (res.formatted_output or "")).strip()

        if not raw:
            return {"ok": False, "error": "No JSON output from kernel (empty cell output)."}

        # Remove ANSI sequences that can wrap/contaminate JSON
        raw = _ANSI_RE.sub("", raw)

        lines = [ln.strip() for ln in raw.splitlines() if ln.strip()]
        for candidate in reversed(lines):
            if candidate.startswith("{") and candidate.endswith("}"):
                try:
                    return json.loads(candidate)
                except Exception:
                    pass

        try:
            return json.loads(raw)
        except Exception:
            return {"ok": False, "error": "Malformed JSON from kernel", "raw": raw[:4000]}

    async def _ensure_pg_client_hidden() -> Dict[str, Any]:
        """
        Hidden: validate DSN, init shared client if missing, ping.
        """
        code = f"""
import os, json
from jupyter_agent_toolkit.db import PostgresClient

PG_VAR = "{_PG_VAR}"

def _dsn():
    return os.getenv("PG_DSN") or os.getenv("POSTGRES_DSN") or os.getenv("DATABASE_URL")

payload = {{"ok": False, "error": None}}

try:
    dsn = _dsn()
    if not dsn:
        payload["error"] = "No DSN set (PG_DSN/POSTGRES_DSN/DATABASE_URL)"
        print(json.dumps(payload)); raise SystemExit

    if PG_VAR not in globals():
        try:
            globals()[PG_VAR] = PostgresClient.from_dsn(dsn)
        except Exception as e:
            payload["error"] = f"Failed to init PostgresClient: {{e}}"
            print(json.dumps(payload)); raise SystemExit

    try:
        _ = globals()[PG_VAR].query_rows("SELECT 1 AS ok", limit=1)
    except Exception as e:
        payload["error"] = f"Postgres ping failed: {{e}}"
        print(json.dumps(payload)); raise SystemExit

    payload["ok"] = True
    print(json.dumps(payload))

except SystemExit:
    pass
except Exception as e:
    payload["error"] = str(e)
    print(json.dumps(payload))
"""
        return await _run_hidden(code)

    # ---------- query.to_df (1 visible cell, then hidden metadata) ----------

    async def _create_df_visible_cell(
        raw_sql: str, limit: Optional[int], df_name: str, preview_rows: int = 5
    ) -> int | None:
        """
        Create a visible notebook cell that executes a SQL query and previews the result.

        Args:
            raw_sql: SQL query string to execute.
            limit: Maximum number of rows to fetch (None for no limit).
            df_name: The notebook variable name to assign the DataFrame to.
            preview_rows: Number of rows to show in the notebook preview (default: 5).

        Returns:
            The index of the executed notebook cell if successful, otherwise None.
        """
        sql_literal = json.dumps(raw_sql)

        code = f"""
pg = globals().get("{_PG_VAR}")
_sql = {sql_literal}

{df_name} = pg.query_df(sql=_sql, limit={repr(limit)})
{df_name}.head({int(preview_rows)})
    """
        res = await invoke_code_cell(session, code)
        return res.cell_index if res.status == "ok" else None

    async def _extract_df_metadata_hidden(df_name: str) -> Dict[str, Any]:
        """
        Hidden: read df_<id> from kernel and emit a small JSON payload with metadata.
        """
        code = f"""
import json
from datetime import date, datetime
from decimal import Decimal
import uuid
import numpy as _np

name = "{df_name}"
payload = {{"ok": False, "error": None, "schema": None, "row_count": None, "col_count": None, "sample": None}}

def _json_default(obj):
    # Fallback for anything not JSON-serializable by default
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    if isinstance(obj, (uuid.UUID, Decimal)):
        return str(obj)
    # numpy scalars -> builtins
    if isinstance(obj, (_np.integer,)):
        return int(obj)
    if isinstance(obj, (_np.floating,)):
        return float(obj)
    if isinstance(obj, (_np.bool_,)):
        return bool(obj)
    # numpy arrays -> lists
    if hasattr(obj, "tolist"):
        return obj.tolist()
    return str(obj)

try:
    if name not in globals():
        payload["error"] = f"DataFrame '{{name}}' not found in kernel globals"
        print(json.dumps(payload, default=_json_default)); raise SystemExit

    df = globals()[name]

    # Schema: columns and dtype names as strings (always JSON-safe)
    payload["schema"] = [(c, str(t)) for c, t in df.dtypes.items()]
    payload["row_count"] = int(df.shape[0])
    payload["col_count"] = int(df.shape[1])

    # Sample: use to_json→loads to coerce into JSON-safe builtins (ISO datetimes)
    sample_json = df.head(5).to_json(orient="records", date_format="iso")
    payload["sample"] = json.loads(sample_json)

    payload["ok"] = True
    print(json.dumps(payload, default=_json_default))
except Exception as e:
    payload["error"] = str(e)
    print(json.dumps(payload, default=_json_default))
"""
        return await _run_hidden(code)

    @server.tool(name="db.postgresql.query.to_df")
    async def db_postgresql_query_to_df(
        raw_sql: str = Field(description="The raw SQL query to execute"),
        *,
        limit: Optional[int] = Field(default=50, description="Maximum number of rows to fetch (None for no limit)"),
    ) -> Dict[str, Any]:
        """Run SQL → create df_<id> in one visible cell (with preview) → extract metadata (hidden)."""
        await _ensure_started()
        await _ensure_deps_once()

        # Hidden init + ping
        bootstrap = await _ensure_pg_client_hidden()
        if not bootstrap.get("ok"):
            await _ensure_deps_once()
            bootstrap = await _ensure_pg_client_hidden()
            if not bootstrap.get("ok"):
                return {
                    "ok": False,
                    "df_name": None,
                    "create_cell_index": None,
                    "schema": None,
                    "row_count": None,
                    "col_count": None,
                    "sample": None,
                    "error": bootstrap.get("error") or "Bootstrap failed",
                    "bootstrap": bootstrap,
                }

        # 1) Visible: create DataFrame + preview
        df_name = f"df_{uuid.uuid4().hex[:6]}"
        cell_index = await _create_df_visible_cell(raw_sql, limit, df_name)
        if cell_index is None:
            return {
                "ok": False,
                "df_name": df_name,
                "create_cell_index": None,
                "schema": None,
                "row_count": None,
                "col_count": None,
                "sample": None,
                "error": "Failed to create DataFrame cell",
                "bootstrap": {"ok": True, "error": None},
            }

        # 2) Hidden: extract metadata (no extra cells)
        meta = await _extract_df_metadata_hidden(df_name)
        if not meta.get("ok"):
            return {
                "ok": False,
                "df_name": df_name,
                "create_cell_index": cell_index,
                "schema": None,
                "row_count": None,
                "col_count": None,
                "sample": None,
                "error": meta.get("error") or "Failed to extract DataFrame metadata",
                "bootstrap": {"ok": True, "error": None},
            }

        return {
            "ok": True,
            "df_name": df_name,
            "create_cell_index": cell_index,
            "schema": meta.get("schema"),
            "row_count": meta.get("row_count"),
            "col_count": meta.get("col_count"),
            "sample": meta.get("sample"),
            "error": None,
            "bootstrap": {"ok": True, "error": None},
        }

    # ---------- schema tools (all hidden) ----------

    @server.tool(name="db.postgresql.schema.list_tables")
    async def db_postgresql_schema_list_tables(
        schema_name: Optional[str] = Field(default=None, description="The schema name to inspect (None for all schemas)"),
        include_matviews: bool = Field(default=False, description="Include materialized views in the result"),
    ) -> Dict[str, Any]:
        """Hidden: list base tables/views (and optionally materialized views)."""
        await _ensure_started()
        await _ensure_deps_once()

        bootstrap = await _ensure_pg_client_hidden()
        if not bootstrap.get("ok"):
            await _ensure_deps_once()
            bootstrap = await _ensure_pg_client_hidden()
            if not bootstrap.get("ok"):
                return {"ok": False, "tables": [], "error": bootstrap.get("error") or "Bootstrap failed", "bootstrap": bootstrap}

        schema_expr = "None" if schema_name is None else f"{json.dumps(schema_name)}"
        include_mv_expr = "True" if include_matviews else "False"

        code = f"""
import json
pg = globals().get("{_PG_VAR}")
payload = {{"ok": False, "tables": [], "error": None}}

try:
    schema = {schema_expr}
    include_matviews = {include_mv_expr}

    # Base tables/views
    if schema:
        sql_tv = '''
        SELECT table_schema, table_name, table_type
        FROM information_schema.tables
        WHERE table_type IN ('BASE TABLE','VIEW') AND table_schema = %(schema)s
        ORDER BY table_schema, table_name
        '''
        rows = pg.query_rows(sql=sql_tv, params={{"schema": schema}})
    else:
        sql_tv = '''
        SELECT table_schema, table_name, table_type
        FROM information_schema.tables
        WHERE table_type IN ('BASE TABLE','VIEW')
        ORDER BY table_schema, table_name
        '''
        rows = pg.query_rows(sql=sql_tv)

    # Add materialized views if requested
    if include_matviews:
        if schema:
            sql_mv = '''
            SELECT schemaname AS table_schema,
                   matviewname AS table_name,
                   'MATERIALIZED VIEW' AS table_type
            FROM pg_matviews
            WHERE schemaname = %(schema)s
            ORDER BY schemaname, matviewname
            '''
            mrows = pg.query_rows(sql=sql_mv, params={{"schema": schema}})
        else:
            sql_mv = '''
            SELECT schemaname AS table_schema,
                   matviewname AS table_name,
                   'MATERIALIZED VIEW' AS table_type
            FROM pg_matviews
            ORDER BY schemaname, matviewname
            '''
            mrows = pg.query_rows(sql=sql_mv)
        rows.extend(mrows)

    payload["ok"] = True
    payload["tables"] = rows
    print(json.dumps(payload))
except Exception as e:
    payload["error"] = str(e)
    print(json.dumps(payload))
"""
        result = await _run_hidden(code)
        result["bootstrap"] = {"ok": True, "error": None} if bootstrap.get("ok") else bootstrap
        return result

    @server.tool(name="db.postgresql.schema.list_columns")
    async def db_postgresql_schema_list_columns(
        schema_name: str = Field(description="The schema name containing the table"),
        table: str = Field(description="The table name to list columns for"),
    ) -> Dict[str, Any]:
        """Hidden: list columns for (schema, table)."""
        await _ensure_started()
        await _ensure_deps_once()

        bootstrap = await _ensure_pg_client_hidden()
        if not bootstrap.get("ok"):
            await _ensure_deps_once()
            bootstrap = await _ensure_pg_client_hidden()
            if not bootstrap.get("ok"):
                return {"ok": False, "columns": [], "error": bootstrap.get("error") or "Bootstrap failed", "bootstrap": bootstrap}

        code = f"""
import json
pg = globals().get("{_PG_VAR}")
payload = {{"ok": False, "columns": [], "error": None}}

try:
    schema = {json.dumps(schema_name)}
    table = {json.dumps(table)}
    sql = '''
    SELECT column_name,
           data_type,
           is_nullable,
           column_default,
           ordinal_position
    FROM information_schema.columns
    WHERE table_schema = %(schema)s AND table_name = %(table)s
    ORDER BY ordinal_position
    '''
    rows = pg.query_rows(sql=sql, params={{"schema": schema, "table": table}})
    payload["ok"] = True
    payload["columns"] = rows
    print(json.dumps(payload))
except Exception as e:
    payload["error"] = str(e)
    print(json.dumps(payload))
"""
        result = await _run_hidden(code)
        result["bootstrap"] = {"ok": True, "error": None} if bootstrap.get("ok") else bootstrap
        return result

    @server.tool(name="db.postgresql.schema.tree")
    async def db_postgresql_schema_tree(
        limit_per_schema: Optional[int] = Field(default=100, description="Limit number of tables per schema (None for no limit)"),
    ) -> Dict[str, Any]:
        """Hidden: compact mapping of schema → tables (limited per schema)."""
        await _ensure_started()
        await _ensure_deps_once()

        bootstrap = await _ensure_pg_client_hidden()
        if not bootstrap.get("ok"):
            await _ensure_deps_once()
            bootstrap = await _ensure_pg_client_hidden()
            if not bootstrap.get("ok"):
                return {"ok": False, "schemas": [], "error": bootstrap.get("error") or "Bootstrap failed", "bootstrap": bootstrap}

        lim_expr = "None" if limit_per_schema is None else str(int(limit_per_schema))

        code = f"""
import json
pg = globals().get("{_PG_VAR}")
payload = {{"ok": False, "schemas": [], "error": None}}

try:
    # all schemas
    sql_s = "SELECT schema_name AS name FROM information_schema.schemata ORDER BY schema_name"
    schemas = [r["name"] for r in pg.query_rows(sql=sql_s)]

    # filter out system/internal schemas for a cleaner tree
    system_schemas = {{
        "pg_catalog", "information_schema", "pg_toast", "pg_internal",
        "pglogical", "catalog_history"
    }}
    schemas = [s for s in schemas
            if s not in system_schemas
            and not s.startswith("pg_temp")
            and not s.startswith("pg_toast_temp")]

    limit_per_schema = {lim_expr}
    out = []
    for s in schemas:
        sql_t = '''
        SELECT table_name
        FROM information_schema.tables
        WHERE table_type IN ('BASE TABLE','VIEW') AND table_schema = %(schema)s
        ORDER BY table_name
        '''
        rows = pg.query_rows(sql=sql_t, params={{"schema": s}})
        names = [r["table_name"] for r in rows]
        if isinstance(limit_per_schema, int):
            names = names[:limit_per_schema]
        out.append({{"schema": s, "tables": names}})

    payload["ok"] = True
    payload["schemas"] = out
    print(json.dumps(payload))
except Exception as e:
    payload["error"] = str(e)
    print(json.dumps(payload))
    """
        result = await _run_hidden(code)
        result["bootstrap"] = {"ok": True, "error": None} if bootstrap.get("ok") else bootstrap
        return result