#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def main():
    for path in sorted(ROOT.rglob("*")):
        if path.is_file():
            print(path.relative_to(ROOT))

if __name__ == "__main__":
    main()
