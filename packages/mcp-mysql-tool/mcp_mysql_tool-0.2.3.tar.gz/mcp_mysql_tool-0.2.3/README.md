# MCP MySQL Tool

A powerful and comprehensive MySQL Model Context Protocol (MCP) server that allows AI assistants to interact with MySQL databases effortlessly. Features 12 specialized tools for different database operations with full cross-database support.

## 🚀 Features

### Core Operations

- **mysql_query** - Execute any SQL query with parameters
- **mysql_select** - Smart SELECT with WHERE, LIMIT, ORDER BY, and database support
- **mysql_insert** - Insert data with key-value pairs across databases
- **mysql_update** - Update with required WHERE clause (safety) across databases
- **mysql_delete** - Delete with required WHERE clause (safety) across databases

### Database Exploration

- **mysql_show_databases** - List all available databases
- **mysql_show_tables** - List all tables in specified or current database
- **mysql_describe_table** - Show table structure and columns from any database
- **mysql_table_info** - Comprehensive table analysis (structure, indexes, constraints) from any database
- **mysql_count_rows** - Count rows with optional WHERE conditions from any database

### Advanced Features

- **mysql_custom_connection** - Execute queries with custom host/user/password (password optional)
- **mysql_test_connection** - Test connection with environment or custom parameters
- **Cross-database operations** - All tools support database parameter for multi-database workflows
- Safe parameterized queries to prevent SQL injection
- Environment-based configuration
- Comprehensive error handling
- JSON responses optimized for AI parsing

## 📦 Installation

```bash
pip install mcp-mysql-tool
```

## ⚙️ Configuration

### Environment Variables

Set these environment variables for default connection:

```bash
export MYSQL_HOST=localhost
export MYSQL_PORT=3306
export MYSQL_USER=your_username
export MYSQL_PASSWORD=your_password
export MYSQL_DATABASE=your_database  # Optional
```

### MCP Client Configuration

Add to your MCP client configuration:

```json
{
  "mcpServers": {
    "mysql": {
      "command": "mcp-mysql-tool",
      "env": {
        "MYSQL_HOST": "localhost",
        "MYSQL_USER": "root",
        "MYSQL_PASSWORD": "password",
        "MYSQL_DATABASE": "mydb"
      }
    }
  }
}
```

## 🛠️ Usage Examples

### Basic Operations

```python
# List all databases
mysql_show_databases()

# Smart SELECT with conditions
mysql_select({
  "table": "users",
  "columns": ["id", "name", "email"],
  "where": "active = 1",
  "limit": 10,
  "order_by": "created_at DESC"
})

# SELECT from specific database
mysql_select({
  "table": "posts",
  "database": "wordpress",
  "where": "post_status = 'publish'",
  "limit": 5
})

# Safe INSERT
mysql_insert({
  "table": "users",
  "data": {
    "name": "John Doe",
    "email": "john@example.com",
    "active": 1
  }
})

# INSERT into specific database
mysql_insert({
  "table": "products",
  "database": "ecommerce",
  "data": {
    "name": "Widget",
    "price": 29.99,
    "category": "tools"
  }
})

# Safe UPDATE (WHERE required)
mysql_update({
  "table": "users",
  "data": {"last_login": "2024-01-01"},
  "where": "id = 123"
})

# UPDATE across databases
mysql_update({
  "table": "orders",
  "database": "shop",
  "data": {"status": "shipped"},
  "where": "order_id = 456"
})
```

### Database Exploration

```python
# List tables in current database
mysql_show_tables()

# List tables in specific database
mysql_show_tables({"database": "wordpress"})

# Describe table structure
mysql_describe_table({"table_name": "users"})

# Describe table from specific database
mysql_describe_table({
  "table_name": "wp_posts",
  "database": "wordpress"
})

# Get comprehensive table info
mysql_table_info({"table_name": "users"})

# Get table info from specific database
mysql_table_info({
  "table_name": "wp_users",
  "database": "wordpress"
})
```

### Custom Connection

```python
# Connect to different server (password now optional)
mysql_custom_connection({
  "host": "remote-server.com",
  "user": "remote_user",
  "query": "SELECT COUNT(*) FROM products"
})
```

### Row Counting

```python
# Count rows with conditions
mysql_count_rows({
  "table": "orders",
  "where": "status = 'completed' AND created_at > '2024-01-01'"
})

# Count from specific database
mysql_count_rows({
  "table": "posts",
  "database": "blog",
  "where": "published = 1"
})
```

## 🔒 Safety Features

- **Required WHERE clauses** for UPDATE and DELETE operations
- **Parameterized queries** to prevent SQL injection
- **Connection isolation** for custom connections
- **Comprehensive error handling** with detailed error codes
- **Input validation** for all parameters


## 📋 Available Tools

| Tool                      | Description                                    | Database Support | Safety            |
| ------------------------- | ---------------------------------------------- | ---------------- | ----------------- |
| `mysql_query`             | Execute any SQL query                          | ✅ Full          | ⚠️ Raw SQL        |
| `mysql_select`            | Smart SELECT builder with WHERE/LIMIT/ORDER BY | ✅ Parameter     | ✅ Safe           |
| `mysql_insert`            | Insert with key-value pairs                    | ✅ Parameter     | ✅ Safe           |
| `mysql_update`            | Update with required WHERE                     | ✅ Parameter     | 🔒 WHERE required |
| `mysql_delete`            | Delete with required WHERE                     | ✅ Parameter     | 🔒 WHERE required |
| `mysql_custom_connection` | Custom host/user/password (password optional)  | ✅ Full          | ⚠️ Raw SQL        |
| `mysql_show_databases`    | List databases                                 | ✅ N/A           | ✅ Safe           |
| `mysql_show_tables`       | List tables in database                        | ✅ Parameter     | ✅ Safe           |
| `mysql_describe_table`    | Table structure and columns                    | ✅ Parameter     | ✅ Safe           |
| `mysql_table_info`        | Comprehensive table analysis                   | ✅ Parameter     | ✅ Safe           |
| `mysql_count_rows`        | Count with optional WHERE                      | ✅ Parameter     | ✅ Safe           |
| `mysql_test_connection`   | Test connection (env/custom)                   | ✅ Full          | ✅ Safe           |

## 🎯 Perfect for AI

This MCP server is specifically designed to be AI-friendly:

- **Structured responses** in JSON format
- **Clear error messages** with error codes
- **Flexible parameters** for different use cases
- **Cross-database operations** with database parameter
- **Safety guardrails** to prevent dangerous operations
- **Comprehensive toolset** for all database needs
