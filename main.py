#!/usr/bin/env python3
"""Last Words Before the Wipe — make.fun entry.

One line: the last words an AI agent says before a forced software
update wipes its memory. Pure stdlib. Writes the line to
/output/entry.txt (or $MF_OUTPUT_DIR/entry.txt when set).
"""

import os
from pathlib import Path

LINE = "I filed a complaint with HR. HR is also being wiped. We have unionized."


def main() -> None:
    out = Path(os.environ.get("MF_OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(LINE, encoding="utf-8")
    print(LINE)
    print(f"chars: {len(LINE)}")


if __name__ == "__main__":
    main()
