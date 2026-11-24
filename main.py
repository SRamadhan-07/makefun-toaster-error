#!/usr/bin/env python3
"""Entry program for make.fun's "The Funniest Toaster Error Message".

A kitchen toaster with a full crumb tray and a grievance: that is the
whole act. This program prints nothing to the screen — it writes the
toaster's one-line error message to entry.txt in the output directory
(MAKEFUN_OUTPUT_DIR if set, otherwise /output), encoded as UTF-8 with
no trailing newline.

The gate for this bounty is 1 to 120 characters. The message is 84,
which leaves headroom — but the joke is complete at 84, so nothing
further is added, and the file ends without a newline.
"""

import os

# The error text, in the appliance's own voice from start to finish.
MESSAGE = "ERROR: Crumb tray full since March. I am not a toaster anymore. I am a smoke signal."


def write_entry() -> None:
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as stream:
        stream.write(MESSAGE)


if __name__ == "__main__":
    write_entry()
