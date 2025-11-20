"""Advent of Code 2024 - Day 02: Red-Nosed Reports."""


def parse(raw: str) -> list[list[int]]:
    return [list(map(int, line.split()))
            for line in raw.splitlines()
            if line.strip()]


def solve_part1(raw: str):
    reports = parse(raw)
    return sum(is_valid_report(r) for r in reports)


def solve_part2(raw: str):
    reports = parse(raw)
    return sum(is_valid_with_dampener(r) for r in reports)


def is_valid_report(report: list[int]) -> bool:
    if len(report) < 2:
        return False

    diffs = [b - a for a, b in zip(report, report[1:])]
    increasing = all(1 <= d <= 3 for d in diffs)
    decreasing = all(-3 <= d <= -1 for d in diffs)
    return increasing or decreasing


def is_valid_with_dampener(report: list[int]) -> bool:
    if is_valid_report(report):
        return True

    for i in range(len(report)):
        shortened = report[:i] + report[i + 1:]
        if is_valid_report(shortened):
            return True

    return False

if __name__ == "__main__":
    from aoc.runner import run_day_from_file

    run_day_from_file(__file__, globals())
