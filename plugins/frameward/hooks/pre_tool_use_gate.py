#!/usr/bin/env python3
from lib.frameward_common import (
    is_dependency_or_provider_activation,
    is_ui_edit_event,
    load_state,
    make_context,
    make_deny,
    read_event,
)
import json

PRE_EDIT_GATES = {"intent", "layout", "system", "ratio"}

def main():
    event = read_event()
    state = load_state()
    if not state.get("active"):
        return

    activation = is_dependency_or_provider_activation(event)
    approvals = state.get("approvals", {})
    if activation == "dependency" and not approvals.get("dependencyInstall"):
        print(json.dumps(make_deny(
            "Frameward blocked a dependency install because the user has not explicitly approved adding dependencies."
        ), ensure_ascii=False))
        return
    if activation == "astryx-mcp" and not approvals.get("astryxMcp"):
        print(json.dumps(make_deny(
            "Frameward blocked Astryx setup or MCP activation because Astryx must stay optional unless the user explicitly approves it."
        ), ensure_ascii=False))
        return

    if not is_ui_edit_event(event):
        return

    mode = state.get("mode", "advisory")
    completed = set(state.get("completedGates", []))
    missing = sorted(PRE_EDIT_GATES - completed)

    if mode in {"strict", "hybrid-strict"} and missing:
        print(json.dumps(make_deny(
            "Frameward pre-edit gate failed. Before editing likely UI files, complete these gates: "
            + ", ".join(missing)
            + ". Write a short intent, screen-area, project-style, and spacing/proportion analysis first."
        ), ensure_ascii=False))
        return

    if missing:
        print(json.dumps(make_context(
            "Frameward advisory: before editing likely UI code, make sure the goal, screen areas, project style rules, and spacing/proportion direction are clear. Missing now: "
            + ", ".join(missing),
            "PreToolUse"
        ), ensure_ascii=False))

if __name__ == "__main__":
    main()
