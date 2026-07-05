#!/usr/bin/env python3
from lib.frameward_common import (
    DEFAULT_REQUIRED_GATES,
    active_config_mode,
    approval_flags,
    complete_gate,
    detect_ui_task,
    detect_vague,
    make_context,
    prompt_from_event,
    read_event,
    save_state,
)
import json

def main():
    event = read_event()
    prompt = prompt_from_event(event)

    if not detect_ui_task(prompt):
        return

    state = {
        "active": True,
        "taskType": "ui-improvement",
        "vague": detect_vague(prompt),
        "requiredGates": DEFAULT_REQUIRED_GATES,
        "completedGates": [],
        "failedGates": [],
        "loopCount": 0,
        "maxLoops": 3,
        "mode": active_config_mode(),
        "provider": "project-native",
        "providerMode": "auto",
        "approvals": approval_flags(prompt),
        "lastChangedFiles": [],
        "originalPrompt": prompt[:1000]
    }
    complete_gate(state, "intent")
    save_state(state)

    message = (
        "Frameward detected a UI-related task. Use plain language, state assumptions, detect the design-system provider, "
        "and avoid expert design terms unless the user uses them first."
    )
    if state["vague"]:
        message += " The request appears vague, so create a short plain-language interpretation before editing."

    print(json.dumps(make_context(message, "UserPromptSubmit"), ensure_ascii=False))

if __name__ == "__main__":
    main()
