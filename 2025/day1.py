"""
Day 1 - 2025
"""

import re

from python.runfiles import Runfiles

INSTRUCTION_RE = re.compile(r"(L|R)(\d+)")


def part1() -> None:
    """We start at 50 and take in a sequence of + and - to reach a final number."""
    r = Runfiles.Create()

    # starting_point = 50
    with open(r.Rlocation("_main/2025/day1_part1_input.txt"), encoding="utf8") as fh:
        instructions = fh.read().strip().splitlines()

    for instruction in instructions:
        direction, amount = INSTRUCTION_RE.match(instruction).groups()
        print(f"Direction: {direction}, Amount: {amount}")


def main() -> None:
    """Entry point"""
    part1()


if __name__ == "__main__":
    main()
