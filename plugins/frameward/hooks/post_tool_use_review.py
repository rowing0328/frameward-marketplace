#!/usr/bin/env python3
from lib.frameward_common import complete_gate, is_ui_edit_event, load_state, make_context, read_event, save_state
import json

def main():
    event = read_event()
    state = load_state()
    if not state.get("active"):
        return

    if not is_ui_edit_event(event):
        return

    complete_gate(state, "implementation")

    save_state(state)

    message = (
        "Frameward post-change review: after UI edits, check mobile behavior, keyboard/focus, empty/loading/error states, "
        "important button visibility, and plain-language explanation."
    )
    print(json.dumps(make_context(message, "PostToolUse"), ensure_ascii=False))

if __name__ == "__main__":
    main()
