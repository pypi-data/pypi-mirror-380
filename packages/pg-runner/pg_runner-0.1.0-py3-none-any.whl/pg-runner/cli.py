#!/usr/bin/env python3
"""
pg-runner: Standalone PostgreSQL database setup and SQL runner.

Features:
-   Configurable DB connection via --db-url or discrete options with env var fallbacks.
-   Two execution modes:
    1) phases (default): project-style phases keyed by a StrEnum with optional single-phase subcommands.
    2) dir: run all .sql files in a directory alphabetically (optionally recursive).
-   Robust SQL splitting (strings, dollar quotes, comments) and detailed logging.
"""

from __future__ import annotations

import argparse
import logging
import os
import re
import sys
import urllib.parse
from collections.abc import Iterable, Mapping
from enum import StrEnum
from pathlib import Path

from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine


# ----------------------------------------------------------------------
# Constants and types
# ----------------------------------------------------------------------
class DBSetupPhase(StrEnum):
    SCHEMA = "schema"
    INDEXES = "indexes"
    VIEWS = "views"


DOLLAR_TAG_RE = re.compile(r"\$[A-Za-z_][A-Za-z0-9_]*\$")


# ----------------------------------------------------------------------
# Logging
# ----------------------------------------------------------------------
def _resolve_log_level(value: str | int) -> int:
    """
    Resolve a logging level from int or string, falling back to INFO.
    Accepts standard names (DEBUG, INFO, WARNING, ERROR, CRITICAL) or integers.
    """
    try:
        if isinstance(value, int):
            return value
        if isinstance(value, str):
            name = value.strip().upper()
            if name.isdigit():
                return int(name)
            return getattr(logging, name, logging.INFO)
    except Exception:
        logging.getLogger(__name__).debug(
            "Failed to resolve log level; defaulting to INFO",
            exc_info=True,
        )
    return logging.INFO


logger = logging.getLogger(__name__)


# ----------------------------------------------------------------------
# DB connection helpers
# ----------------------------------------------------------------------
def _compose_db_url_from_parts(
    user: str | None,
    password: str | None,
    host: str | None,
    port: int | str | None,
    database: str | None,
) -> str:
    """
    Compose a PostgreSQL SQLAlchemy URL from discrete parts.
    """
    user = user or "postgres"
    password = password or ""
    host = host or "localhost"
    port = str(port) if port is not None else "5432"
    database = database or "postgres"

    # URL-encode username/password
    user_enc = urllib.parse.quote(user, safe="")
    pwd_enc = urllib.parse.quote(password, safe="")

    auth = user_enc if not pwd_enc else f"{user_enc}:{pwd_enc}"
    netloc = f"{auth}@{host}:{port}" if auth else f"{host}:{port}"
    return f"postgresql://{netloc}/{database}"


def _determine_db_url(args: argparse.Namespace, env: Mapping[str, str]) -> str:
    """
    Determine the database URL from CLI args or environment variables.
    Precedence:
    1) --db-url
    2) DATABASE_URL or DB_URL
    3) Compose from POSTGRES_* env vars and/or discrete CLI parts
    """
    if getattr(args, "db_url", None):
        return args.db_url

    env_url = env.get("DATABASE_URL") or env.get("DB_URL")
    if env_url:
        return env_url

    # Discrete parts via CLI or POSTGRES_* env
    user = args.user or env.get("POSTGRES_USER")
    password = args.password or env.get("POSTGRES_PASSWORD")
    host = args.host or env.get("POSTGRES_HOST")
    port = args.port or env.get("POSTGRES_PORT")
    database = args.database or env.get("POSTGRES_DB") or env.get("POSTGRES_DATABASE")

    return _compose_db_url_from_parts(user, password, host, port, database)


def _redact_url(url: str) -> str:
    """
    Redact the password component in a DB URL for safe logging.
    """
    try:
        parts = urllib.parse.urlsplit(url)
        username = parts.username or ""
        hostname = parts.hostname or ""
        port = f":{parts.port}" if parts.port else ""
        # Rebuild netloc with redacted password if present
        if parts.password is not None:
            userinfo = f"{username}:***@"
        elif username:
            userinfo = f"{username}@"
        else:
            userinfo = ""
        netloc = f"{userinfo}{hostname}{port}"
        return urllib.parse.urlunsplit(
            (
                parts.scheme,
                netloc,
                parts.path,
                parts.query,
                parts.fragment,
            )
        )
    except Exception:
        # Best-effort fallback: scrub any ':password@' pattern
        return re.sub(r":[^@/]+@", ":***@", url)


def get_engine(db_url: str) -> Engine:
    """
    Create a SQLAlchemy Engine with sensible defaults.
    """
    return create_engine(db_url, pool_pre_ping=True)


def test_connection(engine: Engine) -> bool:
    """
    Quick connection test: execute SELECT 1.
    """
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return True
    except Exception:
        logger.exception("Database connection test failed")
        return False


# ----------------------------------------------------------------------
# SQL file handling and execution
# ----------------------------------------------------------------------
def _read_sql_file(file_path: Path) -> str | None:
    """
    Read a SQL file and return its content or None if missing or unreadable.
    Removes a UTF-8 BOM if present.
    """
    if not file_path.exists():
        logger.warning(f"SQL file not found: {file_path}")
        return None
    try:
        content = file_path.read_text(encoding="utf-8")
        if content.startswith("\ufeff"):
            content = content.lstrip("\ufeff")
        return content
    except Exception:
        logger.exception(f"Failed reading {file_path}")
        return None


def _split_sql_statements(sql: str) -> list[str]:
    """
    Split SQL into individual statements by semicolons, correctly handling:
    - PostgreSQL dollar-quoted strings: $$...$$ and $tag$...$tag$
    - Single-quoted strings (with doubled '' escapes)
    - Double-quoted identifiers (with doubled "" escapes)
    - Line comments: --
    - Block comments: /* ... */

    Returns a list of statements including trailing semicolons. Skips chunks that
    contain no actual SQL (only comments/whitespace).
    """
    if not sql:
        return []

    statements: list[str] = []
    buf: list[str] = []
    append = buf.append

    i = 0
    n = len(sql)

    in_single = False
    in_double = False
    in_block_comment = False
    in_line_comment = False
    dollar_tag: str | None = None
    code_seen = False  # tracks non-comment, non-whitespace content

    while i < n:
        ch = sql[i]
        nxt = sql[i + 1] if i + 1 < n else ""

        # Inside a line comment: consume until newline
        if in_line_comment:
            append(ch)
            if ch == "\n":
                in_line_comment = False
            i += 1
            continue

        # Inside a block comment: consume until */
        if in_block_comment:
            append(ch)
            if ch == "*" and nxt == "/":
                append(nxt)
                i += 2
                in_block_comment = False
            else:
                i += 1
            continue

        # Inside a dollar-quoted string
        if dollar_tag is not None:
            if sql.startswith(dollar_tag, i):
                append(dollar_tag)
                i += len(dollar_tag)
                dollar_tag = None
            else:
                append(ch)
                i += 1
            continue

        # Inside a single-quoted string
        if in_single:
            append(ch)
            # Doubled single-quote escape
            if ch == "'" and nxt == "'":
                append(nxt)
                i += 2
                continue
            if ch == "'":
                in_single = False
            i += 1
            continue

        # Inside a double-quoted identifier
        if in_double:
            append(ch)
            # Doubled double-quote escape
            if ch == '"' and nxt == '"':
                append(nxt)
                i += 2
                continue
            if ch == '"':
                in_double = False
            i += 1
            continue

        # Not inside any string/comment context
        # Start of line comment
        if ch == "-" and nxt == "-":
            append(ch)
            append(nxt)
            i += 2
            in_line_comment = True
            continue

        # Start of block comment
        if ch == "/" and nxt == "*":
            append(ch)
            append(nxt)
            i += 2
            in_block_comment = True
            continue

        # Start of dollar-quoted string ($$ or $tag$)
        if ch == "$":
            m = DOLLAR_TAG_RE.match(sql, i)
            if m:
                token = m.group(0)
                append(token)
                i += len(token)
                dollar_tag = token
                code_seen = True
                continue
            if nxt == "$":
                append("$")
                append("$")
                i += 2
                dollar_tag = "$$"
                code_seen = True
                continue

        # Start of single- or double-quoted regions
        if ch == "'":
            append(ch)
            in_single = True
            code_seen = True
            i += 1
            continue

        if ch == '"':
            append(ch)
            in_double = True
            code_seen = True
            i += 1
            continue

        # Statement boundary (outside comments/strings)
        if ch == ";":
            append(ch)
            stmt = "".join(buf).strip()
            if stmt and code_seen:
                statements.append(stmt)
            buf.clear()
            code_seen = False
            i += 1
            continue

        # Regular character
        append(ch)
        if not ch.isspace():
            code_seen = True
        i += 1

    # Handle any trailing buffer without a semicolon
    tail = "".join(buf).strip()
    if tail and code_seen:
        statements.append(tail)

    return statements


def _execute_statements(engine: Engine, statements: list[str], phase: str) -> None:
    """
    Execute a sequence of SQL statements within a single transaction.
    Any failure will abort the entire batch for the phase.
    """
    if not statements:
        logger.info(f"{phase}: no executable statements found; skipping")
        return

    with engine.begin() as conn:
        for i, stmt in enumerate(statements, start=1):
            try:
                conn.execute(text(stmt))
                logger.debug(f"{phase} [{i}/{len(statements)}]: executed")
            except Exception:
                logger.exception(
                    f"{phase} [{i}/{len(statements)}]: error executing statement"
                )
                logger.debug(f"{phase}: failing statement was:\n{stmt}")
                raise
    logger.info(f"{phase}: executed {len(statements)} statements")


def _execute_non_transactional(
    engine: Engine, statements: list[str], phase: str
) -> None:
    """
    Execute a sequence of SQL statements in autocommit mode.
    Intended for operations that cannot run inside a transaction
    (e.g., CREATE INDEX CONCURRENTLY).
    """
    if not statements:
        logger.info(f"{phase}: no executable statements found; skipping")
        return

    with engine.connect() as base_conn:
        conn = base_conn.execution_options(isolation_level="AUTOCOMMIT")
        for i, stmt in enumerate(statements, start=1):
            try:
                conn.execute(text(stmt))
                logger.debug(f"{phase} [{i}/{len(statements)}]: executed (autocommit)")
            except Exception:
                logger.exception(
                    f"{phase} [{i}/{len(statements)}]: error executing statement"
                )
                logger.debug(f"{phase}: failing statement was:\n{stmt}")
                raise
    logger.info(f"{phase}: executed {len(statements)} statements (autocommit)")


def _has_concurrent_index(statements: Iterable[str]) -> bool:
    """
    Detect presence of CREATE INDEX ... CONCURRENTLY in the statement list.
    """
    for s in statements:
        u = s.upper()
        if "CREATE INDEX" in u and "CONCURRENTLY" in u:
            return True
    return False


# ----------------------------------------------------------------------
# Phase-mode execution (project-style)
# ----------------------------------------------------------------------
def setup_database_phases(
    engine: Engine, db_dir: Path, phases: list[DBSetupPhase], use_concurrent: bool
) -> bool:
    """
    Setup database schema, indexes, and views using project-style phases.
    """
    try:
        phase_configs: dict[DBSetupPhase, dict] = {
            DBSetupPhase.SCHEMA: {
                "file": "schema.sql",
                "required": True,
                "description": "Creating database schema",
                "concurrent": False,
            },
            DBSetupPhase.INDEXES: {
                "file": "indexes.sql",
                "required": False,
                "description": "Creating database indexes",
                "concurrent": use_concurrent,
            },
            DBSetupPhase.VIEWS: {
                "file": "views.sql",
                "required": False,
                "description": "Creating database views",
                "concurrent": False,
            },
        }

        for phase in phases:
            if phase not in phase_configs:
                logger.warning(f"Unknown phase '{phase.value}' skipped")
                continue

            config = phase_configs[phase]
            sql_file = db_dir / config["file"]
            sql_content = _read_sql_file(sql_file)

            if sql_content is None:
                if config["required"]:
                    logger.error(f"{config['file']} is required but was not found.")
                    return False
                logger.info(f"No {config['file']} found; skipping {phase.value} phase.")
                continue

            logger.info(f"{config['description']}...")
            statements = _split_sql_statements(sql_content)

            if not statements:
                logger.info(f"{phase.value}: no executable statements parsed; skipping")
                continue

            # Warn if we might run CONCURRENTLY inside a transaction
            if _has_concurrent_index(statements) and not config["concurrent"]:
                logger.warning(
                    f"{phase.value}: detected CREATE INDEX CONCURRENTLY but autocommit is disabled; "
                    f"these statements will fail inside a transaction"
                )

            if config["concurrent"]:
                _execute_non_transactional(engine, statements, phase.value)
            else:
                _execute_statements(engine, statements, phase.value)

        logger.info("Database setup (phases) completed successfully!")
        return True
    except Exception:
        logger.exception("Database setup (phases) failed")
        return False


# ----------------------------------------------------------------------
# Directory-mode execution (generic)
# ----------------------------------------------------------------------
def run_sql_directory(
    engine: Engine, sql_dir: Path, recursive: bool, autocommit: bool
) -> bool:
    """
    Execute all .sql files in a directory in lexicographic order. Optionally recurse.
    Each file is executed as a batch: transactional by default, or autocommit if requested.
    """
    try:
        if not sql_dir.exists() or not sql_dir.is_dir():
            logger.error(f"SQL directory not found or not a directory: {sql_dir}")
            return False

        pattern = "**/*.sql" if recursive else "*.sql"
        files = sorted(sql_dir.glob(pattern), key=lambda p: str(p).lower())

        if not files:
            logger.warning(f"No .sql files found in {sql_dir} (recursive={recursive})")
            return True  # treat as success with no work

        logger.info(
            f"Found {len(files)} .sql files in {sql_dir} "
            f"(recursive={recursive}); autocommit={autocommit}"
        )

        for idx, file in enumerate(files, start=1):
            rel = file.relative_to(sql_dir)
            phase_label = f"dir:{rel}"
            content = _read_sql_file(file)
            if content is None:
                logger.error(f"Skipping unreadable file: {file}")
                return False

            statements = _split_sql_statements(content)
            if not statements:
                logger.info(f"{phase_label}: no executable statements parsed; skipping")
                continue

            if _has_concurrent_index(statements) and not autocommit:
                logger.warning(
                    f"{phase_label}: detected CREATE INDEX CONCURRENTLY but autocommit is disabled; "
                    f"these statements will fail inside a transaction"
                )

            logger.info(f"Executing [{idx}/{len(files)}]: {rel}")
            if autocommit:
                _execute_non_transactional(engine, statements, phase_label)
            else:
                _execute_statements(engine, statements, phase_label)

        logger.info("SQL directory execution completed successfully!")
        return True
    except Exception:
        logger.exception("SQL directory execution failed")
        return False


# ----------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Standalone PostgreSQL database setup and SQL runner"
    )

    # Common options
    parser.add_argument(
        "--log-level",
        default="INFO",
        help="Logging level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL). Default: INFO",
    )
    parser.add_argument(
        "--no-emoji",
        action="store_true",
        help="Disable emoji output for CI environments",
    )

    # Database connection options (CLI override env)
    db_group = parser.add_argument_group("database connection options")
    db_group.add_argument(
        "--db-url",
        help="SQLAlchemy DB URL (overrides other connection options). "
        "Can also be provided via DATABASE_URL or DB_URL",
    )
    db_group.add_argument(
        "--host",
        help="DB host (default: POSTGRES_HOST or localhost)",
    )
    db_group.add_argument(
        "--port",
        type=int,
        help="DB port (default: POSTGRES_PORT or 5432)",
    )
    db_group.add_argument(
        "--database",
        help="Database name (default: POSTGRES_DB/POSTGRES_DATABASE or postgres)",
    )
    db_group.add_argument(
        "--user",
        help="DB user (default: POSTGRES_USER or postgres)",
    )
    db_group.add_argument(
        "--password",
        help="DB password (default: POSTGRES_PASSWORD or empty)",
    )

    subparsers = parser.add_subparsers(dest="command", metavar="{phases,dir,...}")

    # phases subcommand (default mode)
    phases_parser = subparsers.add_parser(
        "phases",
        help="Run project-style phases (schema, indexes, views)",
    )
    phases_parser.add_argument(
        "--db-dir",
        type=Path,
        default=Path.cwd() / "database",
        help="Directory containing SQL files (default: ./database)",
    )
    phases_parser.add_argument(
        "--phases",
        nargs="*",
        default=[p.value for p in DBSetupPhase],
        choices=[p.value for p in DBSetupPhase],
        help="Phases to execute (default: all phases)",
    )
    phases_parser.add_argument(
        "--concurrent-indexes",
        action="store_true",
        help="Use CONCURRENTLY for index creation (requires autocommit)",
    )

    # Single-phase convenience subcommands (git-like UX)
    subparsers.add_parser("schema", help="Run only the schema phase").set_defaults(
        command="phases", phases=[DBSetupPhase.SCHEMA.value]
    )
    subparsers.add_parser("indexes", help="Run only the indexes phase").set_defaults(
        command="phases", phases=[DBSetupPhase.INDEXES.value]
    )
    subparsers.add_parser("views", help="Run only the views phase").set_defaults(
        command="phases", phases=[DBSetupPhase.VIEWS.value]
    )

    # dir subcommand (generic SQL directory runner)
    dir_parser = subparsers.add_parser(
        "dir",
        help="Run all .sql files in a directory in alphabetical order",
    )
    dir_parser.add_argument(
        "--sql-dir",
        type=Path,
        default=Path.cwd(),
        help="Directory containing .sql files (default: current directory)",
    )
    dir_parser.add_argument(
        "--recursive",
        action="store_true",
        help="Recursively include subdirectories",
    )
    dir_parser.add_argument(
        "--autocommit",
        action="store_true",
        help="Execute statements in autocommit mode (required for CONCURRENTLY)",
    )

    # Default to phases if no subcommand provided
    parser.set_defaults(command="phases")

    return parser.parse_args()


def main() -> None:
    args = parse_args()

    # Configure logging based on CLI
    logging.basicConfig(
        level=_resolve_log_level(args.log_level),
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        force=True,
    )

    success_icon = "✅" if not args.no_emoji else "[SUCCESS]"
    failure_icon = "❌" if not args.no_emoji else "[FAILED]"

    db_url = _determine_db_url(args, os.environ)
    redacted = _redact_url(db_url)

    print("Standalone PostgreSQL Database Setup / SQL Runner")
    print("=" * 50)
    print(f"DB URL: {redacted}")
    print(f"Mode: {args.command}")

    # Build engine and test connection
    engine = get_engine(db_url)
    print("Testing database connection...")
    if not test_connection(engine):
        print(f"{failure_icon} Database connection failed")
        sys.exit(1)
    print("Connection OK")

    # Execute according to mode
    ok = False
    if args.command == "phases":
        phases_vals = getattr(args, "phases", [p.value for p in DBSetupPhase])
        phases_enum = [DBSetupPhase(p) for p in phases_vals]
        db_dir = getattr(args, "db_dir", Path.cwd() / "database")
        use_concurrent = getattr(args, "concurrent_indexes", False)

        print(f"Database directory: {db_dir}")
        print(f"Phases: {', '.join(p.value for p in phases_enum)}")
        if use_concurrent:
            print("Using CONCURRENTLY for index creation")
        print()

        ok = setup_database_phases(engine, db_dir, phases_enum, use_concurrent)

    elif args.command == "dir":
        sql_dir = args.sql_dir
        recursive = args.recursive
        autocommit = args.autocommit

        print(f"SQL directory: {sql_dir} (recursive={recursive})")
        print(f"Autocommit: {autocommit}")
        print()

        ok = run_sql_directory(engine, sql_dir, recursive, autocommit)

    else:
        logger.error(f"Unknown command: {args.command}")
        print(f"{failure_icon} Unknown command: {args.command}")
        sys.exit(2)

    if ok:
        print(f"{success_icon} Completed successfully")
        sys.exit(0)
    else:
        print(f"{failure_icon} Failed")
        sys.exit(1)


if __name__ == "__main__":
    main()
