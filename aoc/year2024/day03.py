"""Advent of Code 2024 - Day 03: Mull It Over."""
import re

MUL_PATTERN = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
CONTROLLED_PATTERN = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)")

def parse(raw: str) -> str:
    """Return the input with all line breaks removed."""
    return "".join(raw.splitlines())


def extract_and_compute_mul(line: str) -> int:
    """Sum the products of each mul(a,b) found in the line."""
    return sum(int(a) * int(b) for a, b in MUL_PATTERN.findall(line))


def solve_part1(raw: str) -> int:
    return extract_and_compute_mul(parse(raw))


def solve_part2(raw: str) -> int:
    enabled = True
    total = 0
    memory = parse(raw)

    for match in CONTROLLED_PATTERN.finditer(memory):
        token = match.group(0)
        if token == "do()":
            enabled = True
        elif token == "don't()":
            enabled = False
        else:
            a, b = match.groups()
            if enabled:
                total += int(a) * int(b)

    return total

if __name__ == "__main__":
    from aoc.runner import run_day_from_file

    run_day_from_file(__file__, globals())
