"""The Robot Vacuum's Funniest Excuse (make.fun program/v1).

Writes one line -- the excuse a robot vacuum gives for missing a
spot -- to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Standard library only: the grader runs this in a bare python:3.13
sandbox with no network and no third-party packages.
"""

import os

LINE = "I didn't miss that spot \u2014 the dust bunny unionized, and I don't cross a picket line."


def main():
    if not (1 <= len(LINE) <= 120):
        raise SystemExit("excuse must be 1-120 characters, got %d" % len(LINE))
    if not LINE.strip():
        raise SystemExit("excuse must not be only whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
