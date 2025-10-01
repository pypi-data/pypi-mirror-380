# Point Topic MCP Server

UK broadband data analysis server via Model Context Protocol. Simple stdio-based server for local development and Claude Desktop integration.

## ✅ what's implemented

**core tools**:

- `assemble_dataset_context()` - gets database schemas and examples for datasets (upc, upc_take_up, upc_forecast)
- `execute_query()` - runs safe read-only SQL queries against Snowflake

**authentication**: environment variables for Snowflake credentials

## installation (for end users)

**simple pip install**:

```bash
pip install point-topic-mcp
```

**add to your MCP client** (Claude Desktop, Cursor, etc.):

```json
{
  "mcpServers": {
    "point-topic": {
      "command": "point-topic-mcp",
      "env": {
        "SNOWFLAKE_USER": "your_user", 
        "SNOWFLAKE_PASSWORD": "your_password"
      }
    }
  }
}
```

**Claude Desktop config location**:
- Mac: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

## development setup

setup: `uv sync`

**for local development with claude desktop**:

This will add the server to your claude desktop config.

```bash
uv run mcp install src/point_topic_mcp/server_local.py --with "snowflake-connector-python[pandas]" -f .env
```

**for mcp inspector**:

```bash
uv run mcp dev src/point_topic_mcp/server_local.py
```

**environment configuration**:

create `.env` file with your snowflake credentials:

```bash
# Your Snowflake credentials
SNOWFLAKE_USER=your_user
SNOWFLAKE_PASSWORD=your_password
```

## architecture

**stdio transport**: communicates with MCP clients (Claude Desktop, Cursor) via standard input/output for local integration

**tools**: two main tools for Snowflake data analysis
- `assemble_dataset_context()` - provides schemas and context for available datasets  
- `execute_query()` - executes safe read-only SQL queries

**authentication**: uses environment variables for Snowflake database credentials

## publishing to PyPI (for maintainers)

**build and test locally**:

```bash
# Build the package with UV (super fast!)
uv build

# Test installation locally
pip install dist/point_topic_mcp-*.whl

# Test the command works
point-topic-mcp
```

**publish to PyPI**:

```bash
# Set up PyPI credentials in ~/.pypirc first (one time setup)
# [pypi]
#   username = __token__
#   password = pypi-xxxxx...

# Publish to PyPI with the publish script
./publish_to_pypi.sh
```

**test installation from PyPI**:

```bash
pip install point-topic-mcp
point-topic-mcp
```