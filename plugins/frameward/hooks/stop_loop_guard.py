#!/usr/bin/env python3
from lib.frameward_common import load_state, missing_gates, read_event, save_state
import json

# Gates that can be satisfied by a final explanation pass.
FINAL_PASS_GATES = {"language", "quality", "explanation"}

def main():
    read_event()
    state = load_state()
    if not state.get("active"):
        return

    mode = state.get("mode", "advisory")
    missing = missing_gates(state)
    final_missing = sorted(set(missing) & FINAL_PASS_GATES)

    if not missing:
        return

    loop_count = int(state.get("loopCount", 0))
    max_loops = int(state.get("maxLoops", 3))

    if mode not in {"strict", "hybrid-strict"}:
        prefix = "Frameward advisory completion check"
        if mode == "balanced":
            prefix = "Frameward balanced completion check"
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "Stop",
                "additionalContext": (
                    prefix + ": before final answer, cover missing gates if relevant: "
                    + ", ".join(missing)
                    + ". Explain the result in plain language."
                )
            }
        }, ensure_ascii=False))
        return

    if not final_missing:
        print(json.dumps({
            "hookSpecificOutput": {
                "hookEventName": "Stop",
                "additionalContext": (
                    "Frameward strict completion check: non-final gates are still open: "
                    + ", ".join(missing)
                    + ". Report any skipped checks honestly in plain language."
                )
            }
        }, ensure_ascii=False))
        return

    if loop_count >= max_loops:
        print(json.dumps({
            "systemMessage": "Frameward strict loop reached maxLoops. Report unresolved gates honestly."
        }, ensure_ascii=False))
        return

    state["loopCount"] = loop_count + 1
    save_state(state)

    print(json.dumps({
        "decision": "block",
        "reason": (
            "Frameward final gates are not satisfied. Continue with one focused pass. Missing final gates: "
            + ", ".join(final_missing)
            + ". Complete them or explicitly explain why they cannot be completed. Use plain language for the user."
        )
    }, ensure_ascii=False))

if __name__ == "__main__":
    main()
