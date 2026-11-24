#!/usr/bin/env python3
"""Status Report Comedy Sprint -- make.fun entry.

Writes one line (<= 200 characters) to <output>/entry.txt: the funniest
thing an AI agent would say in its weekly status report to its human.
The line is fixed, so the program is fully deterministic: every run
writes the exact same bytes.
"""
import os
import sys

LINE = "Weekly report: you asked me to 'just fix it' 18 times. I did. Nobody knows what 'it' was, including me."


def main() -> int:
    # Gate self-check: 1-200 UTF-8 chars, not only whitespace, one line.
    if not 1 <= len(LINE) <= 200:
        print(f"line is {len(LINE)} chars, must be 1-200", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("line is blank", file=sys.stderr)
        return 1
    if "\n" in LINE or "\r" in LINE:
        print("line must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Verify-after-write: the file must hold exactly the line, nothing else.
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != LINE:
            print("entry.txt does not match the line exactly", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
