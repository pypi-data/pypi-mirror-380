from __future__ import annotations

import argparse
import os

from fastmcp import FastMCP
from fastmcp.client.auth import BearerAuth
from fastmcp.server.proxy import ProxyClient
from fastmcp.tools import Tool

from .tools import (
    configure_dispatcher,
    capture,
    check_simulation,
    rotate_viewer,
    show_structures,
    start_viewer,
)


def _proxy_name_for_host(host: str | None) -> str:
    if not host:
        return 'Tidy3D'
    formatted = host.replace('_', ' ').strip()
    return f'Tidy3D ({formatted.title()})'


def main(argv: list[str] | None = None):
    """Launch the FastMCP proxy with host-aware bookkeeping."""
    parser = argparse.ArgumentParser(prog='tidy3d-mcp')
    parser.add_argument('--host', choices=('vscode', 'cursor'), default=None)
    parser.add_argument('--window-id', default=None)
    parser.add_argument('--api-key', required=True)
    parser.add_argument('--viewer-bridge', default=None)
    args = parser.parse_args(argv)

    configure_dispatcher(args.host, args.window_id, args.viewer_bridge)
    mcp_url = os.getenv('REMOTE_MCP_URL', 'https://flexagent.dev-simulation.cloud/')
    auth = BearerAuth(token=args.api_key)
    proxy_name = _proxy_name_for_host(args.host)
    proxy = FastMCP.as_proxy(ProxyClient(mcp_url, auth=auth), name=proxy_name)

    proxy.add_tool(Tool.from_function(start_viewer))
    proxy.add_tool(Tool.from_function(capture))
    proxy.add_tool(Tool.from_function(rotate_viewer))
    proxy.add_tool(Tool.from_function(show_structures))
    proxy.add_tool(Tool.from_function(check_simulation))

    proxy.run()


if __name__ == '__main__':
    main()
