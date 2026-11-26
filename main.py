"""Roast the Smart Fridge - one-line entry.

Writes exactly one deadpan roast line to entry.txt, no trailing newline.
No network, no randomness: the line is a constant, written verbatim.
"""

import os

LINE = "My fridge pings 'door ajar' every time I stare inside it, like it's billing me for hope."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir and os.path.isdir(out_dir):
        path = os.path.join(out_dir, "entry.txt")
    elif os.path.isdir("/output"):
        path = os.path.join("/output", "entry.txt")
    else:
        path = "./entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
