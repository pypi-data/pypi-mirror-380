#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ================================================== #
# This file is a part of PYGPT package               #
# Website: https://pygpt.net                         #
# GitHub:  https://github.com/szczyglis-dev/py-gpt   #
# MIT License                                        #
# Created By  : Marcin Szczygliński                  #
# Updated Date: 2025.09.25 14:00:00                  #
# ================================================== #

from __future__ import annotations
import json
import re
from dataclasses import dataclass
from typing import List, Optional, Tuple, Any, Dict


@dataclass
class RouteDecision:
    route: Optional[str]  # next node id or "end"
    content: str          # human-facing content to display
    raw: str              # raw model output
    valid: bool
    error: Optional[str] = None


def build_router_instruction(
    agent_name: str,
    current_id: str,
    allowed_routes: List[str],
    friendly_map: Dict[str, Any],
) -> str:
    """
    Builds an instruction that forces the model to output JSON with next route and content.

    Additionally, if the provided friendly_map contains role information for any of the
    allowed routes (e.g. friendly_map[id] is a dict with a "role" key), these roles
    are included in the instruction to improve routing. This is optional and included
    only when present and non-empty.
    """
    allowed = ", ".join(allowed_routes)

    # Normalize human-friendly names: accept either a plain string or a dict with
    # common name keys such as "name", "title" or "label".
    def _extract_name(val: Any, default_name: str) -> str:
        if isinstance(val, str):
            return val
        if isinstance(val, dict):
            return str(val.get("name") or val.get("title") or val.get("label") or default_name)
        return default_name

    # Extract names and optional roles for allowed routes, without changing input map semantics.
    friendly_names = {rid: _extract_name(friendly_map.get(rid), rid) for rid in allowed_routes}

    # Roles are optional; include only non-empty strings.
    friendly_roles: Dict[str, str] = {}
    for rid in allowed_routes:
        val = friendly_map.get(rid)
        role_val: Optional[str] = None
        if isinstance(val, dict):
            role_val = val.get("role")
        if isinstance(role_val, str) and role_val.strip():
            friendly_roles[rid] = role_val.strip()

    # Base instruction
    instr = (
        "You are a routing-capable agent in a multi-agent flow.\n"
        f"Your id is: {current_id}, name: {agent_name}.\n"
        "You MUST respond ONLY with a single JSON object and nothing else.\n"
        "Schema:\n"
        '{\n'
        '  "route": "<ID of the next agent from allowed_routes OR the string \'end\'>",\n'
        '  "content": "<final response text for the user (or tool result)>"\n'
        '}\n'
        "Rules:\n"
        f"- allowed_routes: [{allowed}]\n"
        "- If you want to finish the flow, set route to \"end\".\n"
        "- content must contain the user-facing answer (you may include structured data as JSON or Markdown inside content).\n"
        "- Do NOT add any commentary outside of the JSON. No leading or trailing text.\n"
        "- If using tools, still return the final JSON with tool results summarized in content.\n"
        f"- Human-friendly route names: {json.dumps(friendly_names)}\n"
    )

    # Append roles only if any are present (optional).
    if friendly_roles:
        instr += f"- Human-friendly route roles (optional): {json.dumps(friendly_roles)}\n"

    return instr


def _extract_json_block(text: str) -> Optional[str]:
    """
    Extract JSON block from the text. Supports raw JSON or fenced ```json blocks.
    """
    # fenced block
    m = re.search(r"```json\s*(\{.*?\})\s*```", text, flags=re.DOTALL | re.IGNORECASE)
    if m:
        return m.group(1).strip()

    # first JSON object occurrence fallback
    brace_idx = text.find("{")
    if brace_idx != -1:
        # naive attempt to find matching closing brace
        snippet = text[brace_idx:]
        # try to trim trailing content after last closing brace
        last_close = snippet.rfind("}")
        if last_close != -1:
            return snippet[: last_close + 1].strip()
    return None


def parse_route_output(raw_text: str, allowed_routes: List[str]) -> RouteDecision:
    """
    Parse model output enforcing the {route, content} schema.
    """
    text = raw_text.strip()
    candidate = text

    # Try direct JSON parse
    parsed: Optional[Any] = None
    for attempt in range(2):
        try:
            parsed = json.loads(candidate)
            break
        except Exception:
            if attempt == 0:
                block = _extract_json_block(text)
                if block:
                    candidate = block
                    continue
            parsed = None
            break

    if isinstance(parsed, dict):
        route = parsed.get("route")
        content = parsed.get("content", "")
        # Normalize route strings
        if isinstance(route, str):
            route_norm = route.strip().lower()
            if route_norm == "end":
                return RouteDecision(route="end", content=str(content), raw=raw_text, valid=True)
            # exact match against allowed
            if route in allowed_routes:
                return RouteDecision(route=route, content=str(content), raw=raw_text, valid=True)
        return RouteDecision(
            route=None,
            content=str(parsed.get("content", "")),
            raw=raw_text,
            valid=False,
            error=f"Invalid or disallowed route: {route}",
        )

    # Not a valid JSON – fallback, pass through content as-is
    return RouteDecision(route=None, content=raw_text, raw=raw_text, valid=False, error="Malformed JSON")