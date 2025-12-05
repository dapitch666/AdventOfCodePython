"""Advent of Code 2025 - Day 05: Cafeteria."""


def parse(raw: str) -> tuple[list[tuple[int, int]], list[int]]:
    parts = raw.strip().split("\n\n")

    rules: list[tuple[int, int]] = [
        (int(a), int(b))
        for a, b in (line.split("-") for line in parts[0].splitlines())
    ]

    # Merge overlapping/adjacent intervals
    merged: list[list[int]] = []
    for start, end in sorted(rules):
        if not merged or merged[-1][1] < start - 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)

    merged_rules: list[tuple[int, int]] = [(s, e) for s, e in merged]

    available = list(map(int, parts[1].strip().splitlines()))

    return merged_rules, available


def solve_part1(raw: str):
    rules, available = parse(raw)
    return sum(
        1
        for value in available
        if any(start <= value <= end for start, end in rules)
    )


def solve_part2(raw: str):
    rules, _ = parse(raw)
    return sum(end - start + 1 for start, end in rules)


if __name__ == "__main__":
    from aoc.runner import run_day_from_file

    run_day_from_file(__file__, globals())
