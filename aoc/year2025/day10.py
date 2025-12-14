"""Advent of Code 2025 - Day 10: Factory."""

from collections import defaultdict
from itertools import product
from functools import cache


def parse(raw: str):
    machines = []
    for row in raw.splitlines():
        lights, *buttons, joltage = row.split()
        lights = tuple(1 if c == "#" else 0 for c in lights[1:-1])
        buttons = [tuple(map(int, x[1:-1].split(","))) for x in buttons]
        joltage = tuple(map(int, joltage[1:-1].split(",")))
        machines.append((lights, buttons, joltage))
    return machines


def build_patterns(buttons, size):
    effects = {}
    patterns = defaultdict(list)

    for mask in product((0, 1), repeat = len(buttons)):
        delta = [0] * size
        for i, p in enumerate(mask):
            for j in buttons[i]:
                delta[j] += p
        lights = tuple(x % 2 for x in delta)
        effects[mask] = tuple(delta)
        patterns[lights].append(mask)

    return effects, patterns


def solve_part1(raw: str):
    total = 0
    for lights, buttons, _ in parse(raw):
        _, patterns = build_patterns(buttons, len(lights))
        total += min(sum(mask) for mask in patterns[lights])
    return total


def solve_part2(raw: str):
    total = 0
    for lights, buttons, joltage in parse(raw):
        effects, patterns = build_patterns(buttons, len(joltage))

        @cache
        def cost(target):
            if all(x == 0 for x in target):
                return 0
            if any(x < 0 for x in target):
                return float("inf")

            pattern = tuple(x % 2 for x in target)
            best = float("inf")
            for mask in patterns[pattern]:
                delta = effects[mask]
                next_target = tuple((t - d) // 2 for d, t in zip(delta, target))
                best = min(best, sum(mask) + 2 * cost(next_target))
            return best

        total += cost(joltage)

    return total


if __name__ == "__main__":
    from aoc.runner import run_day_from_file

    run_day_from_file(__file__, globals())
