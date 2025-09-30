"""FastMCP 邮件服务器包入口."""

from __future__ import annotations

import argparse

from .server import mcp

__all__ = ["mcp", "main"]


def main() -> None:
    """CLI 入口: 运行 MCP 邮件服务器."""

    parser = argparse.ArgumentParser(
        prog="e2b-fastmcp-server",
        description="E2B sandbox-backed FastMCP server",
    )
    parser.add_argument(
        "--transport",
        default="stdio",
        choices=["stdio"],
        help="服务器使用的传输方式，目前仅支持 stdio。",
    )
    args = parser.parse_args()

    mcp.run(transport=args.transport)

if __name__ == "__main__":
    main()