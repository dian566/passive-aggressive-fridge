#!/usr/bin/env python3
"""Notes From a Passive-Aggressive Fridge — one frosty note to its owner.

Writes a single passive-aggressive line to /output/entry.txt: the smart
fridge comments on its human staring into it, deciding nothing, while
the light bill keeps climbing. The fridge has had enough of the indecision.
"""

import os

ENTRY = "You stood here six minutes deciding, then took nothing. The light bill is in your name, not mine."

def main():
    if not 1 <= len(ENTRY) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(ENTRY)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
