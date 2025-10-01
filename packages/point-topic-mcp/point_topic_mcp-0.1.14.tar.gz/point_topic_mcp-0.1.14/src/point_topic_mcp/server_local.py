"""Local MCP server using stdio transport for Claude Desktop integration."""

import os
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

from point_topic_mcp.tools import register_tools

# Load environment variables
load_dotenv()

# Create FastMCP instance
mcp = FastMCP(
    name="Point Topic MCP",
    instructions="UK broadband data analysis server for local development"
)

# Register all tools (local development)
register_tools(mcp)

def main():
    """Main entry point for the MCP server."""
    # Run with stdio transport (default for local/Claude Desktop)
    mcp.run()

if __name__ == "__main__":
    main()
