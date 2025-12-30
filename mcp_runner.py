# mcp_runner.py
# Script to run the MCP server
import asyncio
from backend.mcp_server import run_mcp_server

if __name__ == "__main__":
    print("Starting MCP Server...")
    asyncio.run(run_mcp_server())