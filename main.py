#!/usr/bin/env python3
"""One-Line Office Jokes — V1.

Writes one single-line joke about office life to /output/entry.txt.

The joke turns on a real office detail (the shared fridge, a Jira ticket,
the daily standup, HR) and lands its laugh in the last few words, as the
bounty brief asks. The program is deterministic: it writes the same text
on every run, uses no network and no dependency outside this repository.
"""

import os
from pathlib import Path

JOKE = (
    "The shared fridge holds a yoghurt from 2019 with its own Jira ticket, "
    "its own daily standup, and, as of this morning, its own promotion "
    "\u2014 HR says it now mentors the new interns."
)


def main() -> None:
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    # UTF-8, no BOM, no trailing newline: exactly one line of 177 code points.
    out.write_text(JOKE, encoding="utf-8", newline="")
    os.chmod(out, 0o644)


if __name__ == "__main__":
    main()
