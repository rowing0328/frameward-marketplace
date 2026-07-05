#!/usr/bin/env python3
from lib.frameward_common import make_context, read_event
import json

def main():
    read_event()
    message = (
        "Frameward policy loaded. For UI tasks, translate vague client language into plain-language intent, "
        "map screen areas before components, detect the project’s existing UI rules first, avoid installing or enabling Astryx unless approved, "
        "and explain results without unnecessary expert design terms."
    )
    print(json.dumps(make_context(message, "SessionStart"), ensure_ascii=False))

if __name__ == "__main__":
    main()
