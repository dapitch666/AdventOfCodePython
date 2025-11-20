"""Advent of Code 2024 - Day 01: Historian Hysteria."""
from collections import Counter
from typing import Tuple, List


def parse(raw: str) -> Tuple[List[int], List[int]]:
    lefts, rights = [], []
    for line in raw.splitlines():
        left, right = map(int, line.split())
        lefts.append(left)
        rights.append(right)
    return lefts, rights


def solve_part1(raw: str):
    lefts, rights = parse(raw)
    ls, rs = sorted(lefts), sorted(rights)
    return sum(abs(r - l) for l, r in zip(ls, rs))


def solve_part2(raw: str):
    lefts, rights = parse(raw)
    lc, rc = Counter(lefts), Counter(rights)
    return sum(n * lc[n] * rc[n] for n in lc)


if __name__ == "__main__":
    from aoc.runner import run_day_from_file

    run_day_from_file(__file__, globals())
