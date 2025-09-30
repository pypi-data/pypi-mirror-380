#!/usr/bin/env python3
"""
Tencent Cloud MCP Server Entry Point

Main entry point for the Tencent Cloud MCP server.
Uses tencentcloud-sdk-python directly - no TCCLI installation required.
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.sdk_server import main as sdk_main

def main():
    """Entry point for the tencent-cloud-mcp command."""
    import asyncio
    asyncio.run(sdk_main())

if __name__ == "__main__":
    main()