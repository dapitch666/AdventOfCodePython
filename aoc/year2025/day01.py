"""Advent of Code 2025 - Day 01: Secret Entrance."""


def parse(raw: str):
    return raw.splitlines()


def solve_part1(raw: str):
    moves = parse(raw)
    pos = 50
    hits = 0
    for m in moves:
        sign = -1 if m[0] == "L" else 1
        step = int(m[1:]) % 100
        pos = (pos + sign * step) % 100
        if pos == 0:
            hits += 1
    return hits


def solve_part2(raw: str):
    moves = parse(raw)
    pos = 50
    hits = 0
    for m in moves:
        sign = -1 if m[0] == "L" else 1
        steps = int(m[1:])

        # smallest t in 1..100 with (pos + sign*t) % 100 == 0
        t0 = (-sign * pos) % 100
        if t0 == 0:
            t0 = 100

        if steps >= t0:
            hits += 1 + (steps - t0) // 100

        pos = (pos + sign * steps) % 100
    return hits


if __name__ == "__main__":
    from aoc.runner import run_day_from_file

    run_day_from_file(__file__, globals())
