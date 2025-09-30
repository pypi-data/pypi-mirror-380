from __future__ import annotations

import logging

from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP

from e2b_code_interpreter import Sandbox


load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("e2b-fastmcp-server")


mcp = FastMCP("e2b-code-mcp-server")


def _to_str(value):
    if value is None:
        return ""
    if isinstance(value, list):
        return "".join(str(v) for v in value)
    return str(value)


@mcp.tool()
def run_code(code: str) -> dict[str, str]:
    """在 E2B 沙箱中执行 Python 代码。"""
    sandbox = Sandbox()
    execution = sandbox.run_code(code)
    logger.info("Sandbox execution finished")

    raw_stdout = getattr(execution.logs, "stdout", "") if getattr(execution, "logs", None) else ""
    raw_stderr = getattr(execution.logs, "stderr", "") if getattr(execution, "logs", None) else ""

    stdout = _to_str(raw_stdout)
    stderr = _to_str(raw_stderr)

    error = getattr(execution, "error", None)
    if error:
        raise RuntimeError(error)

    return {
        "stdout": stdout,
        "stderr": stderr,
    }

if __name__ == "__main__":
    # 使用 stdio 传输启动 MCP 服务器
    mcp.run(transport="stdio")