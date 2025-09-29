import argparse
from .server import mcp


def main() -> None:
    """e2b-fastmcp-server: 使用 E2B 沙箱执行 Python 代码的 MCP 服务。"""
    parser = argparse.ArgumentParser(
        description="Run an MCP server that executes Python code in an E2B sandbox."
    )
    parser.parse_args()
    mcp.run(transport="stdio")


__all__ = ["mcp", "main"]
