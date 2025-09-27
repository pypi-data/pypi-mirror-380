#!/usr/bin/env python3
"""MySQL MCP Server - Simple and efficient MySQL operations for AI."""

import asyncio
import json
import os
import re
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

import mysql.connector
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    Tool,
    TextContent,
)

# Server instance
server = Server("mcp-mysql-server")


IDENTIFIER_RE = re.compile(r"^[0-9A-Za-z$_]+$")


def _format_result(payload: Dict[str, Any]) -> List[TextContent]:
    return [TextContent(type="text", text=json.dumps(payload, indent=2, default=str))]


def _ensure_identifier(identifier: str) -> str:
    """Validate and quote an identifier (optionally qualified with one dot)."""
    if not identifier or identifier.strip() != identifier:
        raise ValueError("Identifier cannot be empty or contain surrounding whitespace")

    parts = identifier.split(".")
    if len(parts) > 2:
        raise ValueError("Identifier may only contain a single qualifier")

    quoted_parts = []
    for part in parts:
        if not IDENTIFIER_RE.match(part):
            raise ValueError(
                "Identifier components must be alphanumeric with optional '_' or '$'"
            )
        quoted_parts.append(f"`{part}`")
    return ".".join(quoted_parts)


def _format_columns(columns: Optional[Sequence[str]]) -> str:
    if not columns:
        return "*"

    formatted: List[str] = []
    for column in columns:
        if column == "*":
            formatted.append("*")
            continue
        if column.endswith(".*"):
            base = column[:-2]
            formatted.append(f"{_ensure_identifier(base)}.*")
            continue
        formatted.append(_ensure_identifier(column))
    return ", ".join(formatted)


def _normalize_table(table: str, database: Optional[str] = None) -> str:
    db_part, table_part = _split_table_parts(table, database)
    table_identifier = _ensure_identifier(table_part)
    if db_part:
        return f"{_ensure_identifier(db_part)}.{table_identifier}"
    return table_identifier


def _split_table_parts(
    table: str, database: Optional[str] = None
) -> Tuple[Optional[str], str]:
    if not table or table.strip() != table:
        raise ValueError("Table name cannot be empty or contain surrounding whitespace")

    if database and "." in table:
        raise ValueError(
            "Provide either a database parameter or a qualified table name, not both"
        )

    if database:
        db_part = database
        table_part = table
    else:
        parts = table.split(".")
        if len(parts) == 1:
            db_part = None
            table_part = parts[0]
        elif len(parts) == 2:
            db_part, table_part = parts
        else:
            raise ValueError("Invalid table format; expected 'table' or 'database.table'")

    if db_part and not IDENTIFIER_RE.match(db_part):
        raise ValueError("Database name contains invalid characters")
    if not IDENTIFIER_RE.match(table_part):
        raise ValueError("Table name contains invalid characters")

    return db_part, table_part


def _apply_query(
    connection: mysql.connector.connection.MySQLConnection,
    query: str,
    params: Optional[Iterable[Any]] = None,
) -> Dict[str, Any]:
    cursor = None
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query, params or ())

        if cursor.with_rows:
            results = cursor.fetchall()
            return {"success": True, "data": results, "row_count": len(results)}

        connection.commit()
        return {
            "success": True,
            "affected_rows": cursor.rowcount,
            "message": "Query executed successfully",
        }
    except mysql.connector.Error as exc:
        if connection.is_connected():
            connection.rollback()
        return {
            "success": False,
            "error": str(exc),
            "error_code": exc.errno if hasattr(exc, "errno") else None,
        }
    except Exception as exc:  # pragma: no cover - defensive safeguard
        if connection.is_connected():
            connection.rollback()
        return {"success": False, "error": f"Connection error: {exc}"}
    finally:
        if cursor:
            cursor.close()


class MySQLConnection:
    """Simple MySQL connection manager with automatic reconnect."""

    def __init__(self):
        self.connection: Optional[mysql.connector.connection.MySQLConnection] = None
        self.config = {
            "host": os.getenv("MYSQL_HOST", "localhost"),
            "port": int(os.getenv("MYSQL_PORT", "3306")),
            "user": os.getenv("MYSQL_USER", "root"),
            "password": os.getenv("MYSQL_PASSWORD", ""),
        }
        db_name = os.getenv("MYSQL_DATABASE", "")
        if db_name:
            self.config["database"] = db_name

    def connect(self) -> mysql.connector.connection.MySQLConnection:
        """Establish or reuse a database connection, reconnecting if needed."""
        if self.connection and self.connection.is_connected():
            try:
                self.connection.ping(reconnect=True, attempts=3, delay=2)
                return self.connection
            except mysql.connector.Error:
                self.close()

        self.connection = mysql.connector.connect(**self.config)
        return self.connection

    def close(self) -> None:
        if self.connection and self.connection.is_connected():
            self.connection.close()
        self.connection = None

    def execute_query(
        self, query: str, params: Optional[Iterable[Any]] = None
    ) -> Dict[str, Any]:
        connection = self.connect()
        return _apply_query(connection, query, params)


# Global connection instance - will be initialized when first used
db = None


def get_db():
    """Get database connection instance."""
    global db
    if db is None:
        db = MySQLConnection()
    return db


def execute_with_custom_connection(
    config: Dict[str, Any], query: str, params: Optional[Iterable[Any]] = None
) -> Dict[str, Any]:
    """Execute query with custom connection parameters."""
    connection = None
    try:
        # Create connection config
        conn_config = {
            "host": config["host"],
            "port": config.get("port", 3306),
            "user": config["user"],
            "password": config["password"],
        }
        if config.get("database"):
            conn_config["database"] = config["database"]

        connection = mysql.connector.connect(**conn_config)
        return _apply_query(connection, query, params)
    except mysql.connector.Error as exc:
        return {
            "success": False,
            "error": str(exc),
            "error_code": exc.errno if hasattr(exc, "errno") else None,
        }
    except Exception as exc:
        return {"success": False, "error": f"Connection error: {exc}"}
    finally:
        if connection and connection.is_connected():
            connection.close()


def build_select_query(
    table: str,
    columns: Optional[Sequence[str]] = None,
    where: Optional[str] = None,
    limit: Optional[int] = None,
    order_by: Optional[str] = None,
    database: Optional[str] = None,
) -> str:
    """Build a SELECT query from parameters."""
    table_ref = _normalize_table(table, database)
    cols = _format_columns(columns)
    query = f"SELECT {cols} FROM {table_ref}"

    if where:
        query += f" WHERE {where}"
    if order_by:
        query += f" ORDER BY {order_by}"
    if limit:
        query += f" LIMIT {limit}"

    return query


def build_insert_query(
    table: str, data: Dict[str, Any], database: Optional[str] = None
) -> Tuple[str, Tuple[Any, ...]]:
    """Build an INSERT query from parameters."""
    if not data:
        raise ValueError("Insert data cannot be empty")

    table_ref = _normalize_table(table, database)
    columns = list(data.keys())
    values = list(data.values())
    placeholders = ", ".join(["%s"] * len(values))
    column_clause = ", ".join(_ensure_identifier(col) for col in columns)

    query = f"INSERT INTO {table_ref} ({column_clause}) VALUES ({placeholders})"
    return query, tuple(values)


def build_update_query(
    table: str, data: Dict[str, Any], where: str, database: Optional[str] = None
) -> Tuple[str, Tuple[Any, ...]]:
    """Build an UPDATE query from parameters."""
    if not data:
        raise ValueError("Update data cannot be empty")
    if not where:
        raise ValueError("WHERE clause is required for updates")

    table_ref = _normalize_table(table, database)
    set_clause = ", ".join([f"{_ensure_identifier(col)} = %s" for col in data.keys()])
    values = list(data.values())

    query = f"UPDATE {table_ref} SET {set_clause} WHERE {where}"
    return query, tuple(values)


def build_delete_query(
    table: str, where: str, database: Optional[str] = None
) -> str:
    if not where:
        raise ValueError("WHERE clause is required for deletes")
    table_ref = _normalize_table(table, database)
    return f"DELETE FROM {table_ref} WHERE {where}"


def test_mysql_connection(config: Dict[str, Any] = None) -> Dict[str, Any]:
    """Test MySQL connection and return detailed information."""
    connection = None
    cursor = None

    try:
        # Use provided config or fall back to environment/default config
        if config:
            conn_config = {
                "host": config.get("host", os.getenv("MYSQL_HOST", "localhost")),
                "port": config.get("port", int(os.getenv("MYSQL_PORT", "3306"))),
                "user": config.get("user", os.getenv("MYSQL_USER", "root")),
                "password": config.get("password", os.getenv("MYSQL_PASSWORD", "")),
            }
            if config.get("database") or os.getenv("MYSQL_DATABASE"):
                conn_config["database"] = config.get(
                    "database", os.getenv("MYSQL_DATABASE", "")
                )
        else:
            # Use default connection config
            conn_config = {
                "host": os.getenv("MYSQL_HOST", "localhost"),
                "port": int(os.getenv("MYSQL_PORT", "3306")),
                "user": os.getenv("MYSQL_USER", "root"),
                "password": os.getenv("MYSQL_PASSWORD", ""),
            }
            db_name = os.getenv("MYSQL_DATABASE", "")
            if db_name:
                conn_config["database"] = db_name

        # Attempt connection
        connection = mysql.connector.connect(**conn_config)
        cursor = connection.cursor(dictionary=True)

        # Get connection information
        cursor.execute(
            "SELECT VERSION() as mysql_version, DATABASE() as current_database, USER() as `current_user`, CONNECTION_ID() as connection_id"
        )
        info = cursor.fetchone()

        # Get server status
        cursor.execute("SHOW STATUS LIKE 'Uptime'")
        uptime_result = cursor.fetchone()
        uptime_seconds = int(uptime_result["Value"]) if uptime_result else 0
        uptime_hours = uptime_seconds // 3600
        uptime_days = uptime_hours // 24

        # Test basic operations
        cursor.execute("SELECT 1 as test_query")
        test_result = cursor.fetchone()

        return {
            "success": True,
            "connection_info": {
                "host": conn_config["host"],
                "port": conn_config["port"],
                "user": conn_config["user"],
                "database": conn_config.get("database", "None"),
                "mysql_version": info.get("mysql_version"),
                "current_database": info.get("current_database") or "None",
                "current_user": info.get("current_user"),
                "connection_id": info.get("connection_id"),
                "server_uptime_days": uptime_days,
                "server_uptime_hours": uptime_hours % 24,
                "test_query_result": (
                    test_result.get("test_query") if test_result else None
                ),
            },
            "message": "Connection successful",
        }

    except mysql.connector.Error as e:
        return {
            "success": False,
            "error": str(e),
            "error_code": e.errno if hasattr(e, "errno") else None,
            "connection_config": {
                "host": conn_config.get("host", "unknown"),
                "port": conn_config.get("port", "unknown"),
                "user": conn_config.get("user", "unknown"),
                "database": conn_config.get("database", "None"),
            },
        }
    except Exception as e:
        return {
            "success": False,
            "error": f"Connection error: {str(e)}",
            "connection_config": {
                "host": (
                    conn_config.get("host", "unknown")
                    if "conn_config" in locals()
                    else "unknown"
                ),
                "port": (
                    conn_config.get("port", "unknown")
                    if "conn_config" in locals()
                    else "unknown"
                ),
                "user": (
                    conn_config.get("user", "unknown")
                    if "conn_config" in locals()
                    else "unknown"
                ),
                "database": (
                    conn_config.get("database", "None")
                    if "conn_config" in locals()
                    else "None"
                ),
            },
        }
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()


@server.list_tools()
async def list_tools() -> List[Tool]:
    """List available MySQL tools."""
    return [
        Tool(
            name="mysql_query",
            description="Execute a MySQL query (SELECT, INSERT, UPDATE, DELETE, etc.)",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The SQL query to execute",
                    },
                    "params": {
                        "type": "array",
                        "description": "Optional parameters for prepared statements",
                        "items": {"type": "string"},
                    },
                },
                "required": ["query"],
            },
        ),
        Tool(
            name="mysql_select",
            description="Execute a SELECT query with optional WHERE conditions",
            inputSchema={
                "type": "object",
                "properties": {
                    "table": {
                        "type": "string",
                        "description": "Table name to select from",
                    },
                    "database": {
                        "type": "string",
                        "description": "Database name (optional, uses current or default database)",
                    },
                    "columns": {
                        "type": "array",
                        "description": "Columns to select (default: all columns)",
                        "items": {"type": "string"},
                    },
                    "where": {
                        "type": "string",
                        "description": "WHERE clause (without WHERE keyword)",
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of rows to return",
                    },
                    "order_by": {
                        "type": "string",
                        "description": "ORDER BY clause (without ORDER BY keyword)",
                    },
                },
                "required": ["table"],
            },
        ),
        Tool(
            name="mysql_insert",
            description="Insert data into a table",
            inputSchema={
                "type": "object",
                "properties": {
                    "table": {
                        "type": "string",
                        "description": "Table name to insert into",
                    },
                    "database": {
                        "type": "string",
                        "description": "Database name (optional, uses current or default database)",
                    },
                    "data": {
                        "type": "object",
                        "description": "Key-value pairs of column names and values",
                    },
                },
                "required": ["table", "data"],
            },
        ),
        Tool(
            name="mysql_update",
            description="Update data in a table",
            inputSchema={
                "type": "object",
                "properties": {
                    "table": {"type": "string", "description": "Table name to update"},
                    "database": {
                        "type": "string",
                        "description": "Database name (optional, uses current or default database)",
                    },
                    "data": {
                        "type": "object",
                        "description": "Key-value pairs of column names and new values",
                    },
                    "where": {
                        "type": "string",
                        "description": "WHERE clause (without WHERE keyword) - REQUIRED for safety",
                    },
                },
                "required": ["table", "data", "where"],
            },
        ),
        Tool(
            name="mysql_delete",
            description="Delete data from a table",
            inputSchema={
                "type": "object",
                "properties": {
                    "table": {
                        "type": "string",
                        "description": "Table name to delete from",
                    },
                    "database": {
                        "type": "string",
                        "description": "Database name (optional, uses current or default database)",
                    },
                    "where": {
                        "type": "string",
                        "description": "WHERE clause (without WHERE keyword) - REQUIRED for safety",
                    },
                },
                "required": ["table", "where"],
            },
        ),
        Tool(
            name="mysql_custom_connection",
            description="Execute a query with custom connection parameters",
            inputSchema={
                "type": "object",
                "properties": {
                    "host": {"type": "string", "description": "MySQL host"},
                    "port": {
                        "type": "integer",
                        "description": "MySQL port (default: 3306)",
                    },
                    "user": {"type": "string", "description": "MySQL username"},
                    "password": {
                        "type": "string",
                        "description": "MySQL password (optional, defaults to empty)",
                    },
                    "database": {
                        "type": "string",
                        "description": "Database name (optional)",
                    },
                    "query": {"type": "string", "description": "SQL query to execute"},
                    "params": {
                        "type": "array",
                        "description": "Optional parameters for prepared statements",
                        "items": {"type": "string"},
                    },
                },
                "required": ["host", "user", "query"],
            },
        ),
        Tool(
            name="mysql_show_tables",
            description="Show all tables in the specified database or current database",
            inputSchema={
                "type": "object",
                "properties": {
                    "database": {
                        "type": "string",
                        "description": "Database name (optional, uses current database)",
                    }
                },
            },
        ),
        Tool(
            name="mysql_describe_table",
            description="Describe the structure of a specific table",
            inputSchema={
                "type": "object",
                "properties": {
                    "table_name": {
                        "type": "string",
                        "description": "Name of the table to describe",
                    },
                    "database": {
                        "type": "string",
                        "description": "Database name (optional, uses current or default database)",
                    },
                },
                "required": ["table_name"],
            },
        ),
        Tool(
            name="mysql_show_databases",
            description="Show all available databases",
            inputSchema={"type": "object", "properties": {}},
        ),
        Tool(
            name="mysql_table_info",
            description="Get comprehensive information about a table (structure, indexes, constraints)",
            inputSchema={
                "type": "object",
                "properties": {
                    "table_name": {
                        "type": "string",
                        "description": "Name of the table to analyze",
                    },
                    "database": {
                        "type": "string",
                        "description": "Database name (optional, uses current or default database)",
                    },
                },
                "required": ["table_name"],
            },
        ),
        Tool(
            name="mysql_count_rows",
            description="Count rows in a table with optional WHERE condition",
            inputSchema={
                "type": "object",
                "properties": {
                    "table": {
                        "type": "string",
                        "description": "Table name to count rows from",
                    },
                    "database": {
                        "type": "string",
                        "description": "Database name (optional, uses current or default database)",
                    },
                    "where": {
                        "type": "string",
                        "description": "WHERE clause (without WHERE keyword)",
                    },
                },
                "required": ["table"],
            },
        ),
        Tool(
            name="mysql_test_connection",
            description="Test MySQL connection with current environment config or custom parameters",
            inputSchema={
                "type": "object",
                "properties": {
                    "host": {
                        "type": "string",
                        "description": "MySQL host (optional, uses env MYSQL_HOST if not provided)",
                    },
                    "port": {
                        "type": "integer",
                        "description": "MySQL port (optional, uses env MYSQL_PORT or 3306)",
                    },
                    "user": {
                        "type": "string",
                        "description": "MySQL username (optional, uses env MYSQL_USER if not provided)",
                    },
                    "password": {
                        "type": "string",
                        "description": "MySQL password (optional, uses env MYSQL_PASSWORD if not provided)",
                    },
                    "database": {
                        "type": "string",
                        "description": "Database name (optional, uses env MYSQL_DATABASE if not provided)",
                    },
                },
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: Dict[str, Any]) -> List[TextContent]:
    """Handle tool calls."""

    if name == "mysql_query":
        query = arguments.get("query", "")
        params = arguments.get("params", [])

        if not query:
            return [TextContent(type="text", text="Error: Query parameter is required")]

        result = get_db().execute_query(query, tuple(params) if params else None)
        return _format_result(result)

    elif name == "mysql_select":
        table = arguments.get("table", "")
        database = arguments.get("database")
        if not table:
            return [TextContent(type="text", text="Error: table parameter is required")]

        columns = arguments.get("columns", [])
        where = arguments.get("where")
        limit = arguments.get("limit")
        order_by = arguments.get("order_by")

        try:
            query = build_select_query(
                table,
                columns=columns,
                where=where,
                limit=limit,
                order_by=order_by,
                database=database,
            )
        except ValueError as exc:
            return _format_result({"success": False, "error": str(exc)})

        result = get_db().execute_query(query)
        return _format_result(result)

    elif name == "mysql_insert":
        table = arguments.get("table", "")
        database = arguments.get("database")
        data = arguments.get("data", {})

        if not table or not data:
            return [
                TextContent(
                    type="text", text="Error: table and data parameters are required"
                )
            ]
        try:
            query, params = build_insert_query(table, data, database=database)
        except ValueError as exc:
            return _format_result({"success": False, "error": str(exc)})

        result = get_db().execute_query(query, params)
        return _format_result(result)

    elif name == "mysql_update":
        table = arguments.get("table", "")
        database = arguments.get("database")
        data = arguments.get("data", {})
        where = arguments.get("where", "")

        if not table or not data or not where:
            return [
                TextContent(
                    type="text",
                    text="Error: table, data, and where parameters are required for safety",
                )
            ]
        try:
            query, params = build_update_query(
                table, data, where, database=database
            )
        except ValueError as exc:
            return _format_result({"success": False, "error": str(exc)})

        result = get_db().execute_query(query, params)
        return _format_result(result)

    elif name == "mysql_delete":
        table = arguments.get("table", "")
        database = arguments.get("database")
        where = arguments.get("where", "")

        if not table or not where:
            return [
                TextContent(
                    type="text",
                    text="Error: table and where parameters are required for safety",
                )
            ]
        try:
            query = build_delete_query(table, where, database=database)
        except ValueError as exc:
            return _format_result({"success": False, "error": str(exc)})

        result = get_db().execute_query(query)
        return _format_result(result)

    elif name == "mysql_custom_connection":
        host = arguments.get("host", "")
        user = arguments.get("user", "")
        password = arguments.get("password", "")
        query = arguments.get("query", "")

        if not all([host, user, query]):
            return [
                TextContent(
                    type="text",
                    text="Error: host, user, and query parameters are required",
                )
            ]

        config = {
            "host": host,
            "port": arguments.get("port", 3306),
            "user": user,
            "password": password,
            "database": arguments.get("database", ""),
        }

        params = arguments.get("params", [])
        result = execute_with_custom_connection(
            config, query, tuple(params) if params else None
        )
        return _format_result(result)

    elif name == "mysql_show_tables":
        database = arguments.get("database")
        try:
            if database:
                query = f"SHOW TABLES FROM {_ensure_identifier(database)}"
            else:
                query = "SHOW TABLES"
        except ValueError as exc:
            return _format_result({"success": False, "error": str(exc)})

        result = get_db().execute_query(query)
        return _format_result(result)

    elif name == "mysql_describe_table":
        table_name = arguments.get("table_name", "")
        database = arguments.get("database")
        if not table_name:
            return [
                TextContent(type="text", text="Error: table_name parameter is required")
            ]
        try:
            table_ref = _normalize_table(table_name, database)
        except ValueError as exc:
            return _format_result({"success": False, "error": str(exc)})

        result = get_db().execute_query(f"DESCRIBE {table_ref}")
        return _format_result(result)

    elif name == "mysql_show_databases":
        result = get_db().execute_query("SHOW DATABASES")
        return _format_result(result)

    elif name == "mysql_table_info":
        table_name = arguments.get("table_name", "")
        database = arguments.get("database")
        if not table_name:
            return [
                TextContent(type="text", text="Error: table_name parameter is required")
            ]
        try:
            _, table_part = _split_table_parts(table_name, database)
            table_ref = _normalize_table(table_name, database)
        except ValueError as exc:
            return _format_result({"success": False, "error": str(exc)})

        info: Dict[str, Any] = {}

        # Table structure
        info["structure"] = get_db().execute_query(f"DESCRIBE {table_ref}")

        # Table indexes
        info["indexes"] = get_db().execute_query(f"SHOW INDEX FROM {table_ref}")

        # Table status (use parameterized LIKE for base table name)
        status_query = "SHOW TABLE STATUS LIKE %s"
        status_result = get_db().execute_query(status_query, (table_part,))
        info["status"] = status_result

        return _format_result(info)

    elif name == "mysql_count_rows":
        table = arguments.get("table", "")
        database = arguments.get("database")
        if not table:
            return [TextContent(type="text", text="Error: table parameter is required")]
        try:
            table_ref = _normalize_table(table, database)
        except ValueError as exc:
            return _format_result({"success": False, "error": str(exc)})

        where = arguments.get("where")
        query = f"SELECT COUNT(*) as row_count FROM {table_ref}"
        if where:
            query += f" WHERE {where}"

        result = get_db().execute_query(query)
        return _format_result(result)

    elif name == "mysql_test_connection":
        # Extract custom config if provided
        custom_config = {}
        if arguments.get("host"):
            custom_config["host"] = arguments["host"]
        if arguments.get("port"):
            custom_config["port"] = arguments["port"]
        if arguments.get("user"):
            custom_config["user"] = arguments["user"]
        if arguments.get("password"):
            custom_config["password"] = arguments["password"]
        if arguments.get("database"):
            custom_config["database"] = arguments["database"]

        # Test connection with custom config or environment config
        result = test_mysql_connection(custom_config if custom_config else None)
        return _format_result(result)

    else:
        return [TextContent(type="text", text=f"Error: Unknown tool '{name}'")]


async def main():
    """Run the MySQL MCP server."""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream, write_stream, server.create_initialization_options()
        )


def cli_main():
    """CLI entry point."""
    asyncio.run(main())


if __name__ == "__main__":
    cli_main()
