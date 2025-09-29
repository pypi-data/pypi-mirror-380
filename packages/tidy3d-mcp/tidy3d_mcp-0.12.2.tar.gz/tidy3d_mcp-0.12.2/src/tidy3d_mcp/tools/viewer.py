from __future__ import annotations

import json
from collections.abc import Iterable
from typing import Any

from fastmcp.exceptions import ToolError

from ..utils import ensure_file_uri
from ._dispatcher import invoke_viewer_command
from ._viewers import forget, is_focus_only, remember


def _normalize_visibility(entry: object) -> bool:
    if isinstance(entry, bool):
        return entry
    if entry is None:
        return False
    if isinstance(entry, (int, float)):
        return entry != 0
    if isinstance(entry, str):
        value = entry.strip().lower()
        if value in {'true', '1', 'yes', 'on'}:
            return True
        if value in {'false', '0', 'no', 'off', ''}:
            return False
    return bool(entry)


def _normalize_warnings(raw: object) -> list[str] | None:
    if not raw:
        return None
    if isinstance(raw, str):
        return [raw]
    if isinstance(raw, Iterable):
        normalized = [str(item) for item in raw if item]
        return normalized or None
    return [str(raw)]


async def start_viewer(
    file: str,
    symbol: str | None = None,
    index: int | None = None,
) -> dict[str, Any]:
    """Open the Tidy3D viewer for a simulation definition.

    Args:
        file: Absolute path or workspace-relative URI pointing to a simulation script or notebook.
        symbol: Optional variable name selecting a `tidy3d.Simulation` object inside the file.
        index: Optional zero-based simulation index when multiple simulations are detected.

    Returns:
        Mapping with the resolved ``viewer_id`` plus optional ``status`` and ``warnings``.
    """
    if not file:
        raise ValueError('file is required')
    params: dict[str, object | None] = {'file': ensure_file_uri(file)}
    if symbol:
        params['symbol'] = symbol
    if index is not None:
        params['index'] = index
    result = invoke_viewer_command('start', 'ready', params, timeout=10.0)
    error_msg = result.get('error')
    if isinstance(error_msg, str) and error_msg:
        raise ToolError(f'viewer reported error: {error_msg}')
    viewer_id = result.get('viewer_id')
    if not isinstance(viewer_id, str) or not viewer_id:
        raise ValueError('viewer did not confirm readiness')
    response: dict[str, Any] = {'viewer_id': viewer_id}
    status = result.get('status')
    if isinstance(status, str) and status:
        response['status'] = status
    focusable = isinstance(status, str) and status.lower() == 'focused'
    remember(viewer_id, focusable=focusable)
    warnings = _normalize_warnings(result.get('warnings') or result.get('warning'))
    if warnings:
        response['warnings'] = warnings
    return response


async def rotate_viewer(
    viewer_id: str,
    direction: str,
) -> dict[str, Any]:
    """Align the viewer camera with a principal axis.

    Args:
        viewer_id: Identifier returned by :func:`start_viewer`.
        direction: One of ``TOP``, ``BOTTOM``, ``LEFT``, ``RIGHT``, ``FRONT``, ``BACK`` (case-insensitive).

    Returns:
        Mapping containing ``viewer_id``, the normalized ``direction`` and the reported status string.
    """
    if not viewer_id:
        raise ValueError('viewer_id is required')
    if not direction:
        raise ValueError('direction is required')
    normalized = direction.upper()
    allowed = {'TOP', 'BOTTOM', 'LEFT', 'RIGHT', 'FRONT', 'BACK'}
    if normalized not in allowed:
        raise ValueError(f'direction must be one of {sorted(allowed)}')
    params: dict[str, object | None] = {'viewer': viewer_id, 'direction': normalized}
    result = invoke_viewer_command('rotate', 'rotate', params, timeout=10.0)
    error_msg = result.get('error')
    if isinstance(error_msg, str) and error_msg:
        if is_focus_only(viewer_id):
            forget(viewer_id)
        raise ToolError(f'rotation failed: {error_msg}')
    status = result.get('status', 'ok')
    return {'viewer_id': viewer_id, 'direction': normalized, 'status': status}


async def show_structures(
    viewer_id: str,
    visibility: list[bool],
) -> dict[str, Any]:
    """Toggle structure visibility in the viewer panel.

    Args:
        viewer_id: Identifier returned by :func:`start_viewer`.
        visibility: Boolean flags applied in declaration order of the simulation structures.

    Returns:
        Mapping containing ``viewer_id``, status and the echoed visibility list.
    """
    if not viewer_id:
        raise ValueError('viewer_id is required')
    flags = [_normalize_visibility(entry) for entry in visibility]
    payload = json.dumps(flags)
    params: dict[str, object | None] = {'viewer': viewer_id, 'visibility': payload}
    result = invoke_viewer_command('visibility', 'visibility', params, timeout=10.0)
    error_msg = result.get('error')
    if isinstance(error_msg, str) and error_msg:
        if is_focus_only(viewer_id):
            forget(viewer_id)
        raise ToolError(f'visibility update failed: {error_msg}')
    response: dict[str, Any] = {'viewer_id': viewer_id, 'status': result.get('status', 'ok')}
    returned_flags = result.get('visibility')
    if isinstance(returned_flags, list):
        response['visibility'] = [_normalize_visibility(entry) for entry in returned_flags]
    return response


async def check_simulation(viewer_id: str) -> dict[str, Any]:
    """Return viewer validation state as a mapping with ``status`` plus optional ``warnings`` or ``error``."""
    if not viewer_id:
        raise ValueError('viewer_id is required')
    params: dict[str, object | None] = {'viewer': viewer_id}
    result = invoke_viewer_command('check', 'check', params, timeout=10.0)
    response: dict[str, Any] = {}
    warnings = _normalize_warnings(result.get('warnings'))
    if warnings is not None:
        response['warnings'] = warnings
    error_msg = result.get('error')
    if isinstance(error_msg, str) and error_msg:
        response['error'] = error_msg
    if 'error' in response:
        response['status'] = 'error'
    elif 'warnings' in response:
        response['status'] = 'warning'
    else:
        response['status'] = 'ok'
    return response
