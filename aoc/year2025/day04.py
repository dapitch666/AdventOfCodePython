"""Advent of Code 2025 - Day 04: Printing Department."""
from aoc.utils.grid import neighbors8, parse_grid, in_bounds, get

def parse(raw: str) -> tuple[list[list[str]], tuple[int, int]]:
    rolls = [list(row) for row in parse_grid(raw) if row]
    w, h = len(rolls[0]), len(rolls)
    return rolls, (w, h)


def solve_part1(raw: str):
    rolls, (w, h) = parse(raw)
    return sum(
        1
        for r in range(h)
        for c in range(w)
        if rolls[r][c] == '@' and _is_free_to_remove(rolls, r, c, w, h)
    )


def solve_part2(raw: str):
    rolls, (w, h) = parse(raw)
    total = 0
    while True:
        to_remove = [
            (r, c)
            for r in range(h)
            for c in range(w)
            if rolls[r][c] == '@' and _is_free_to_remove(rolls, r, c, w, h)
        ]
        total += len(to_remove)
        if not to_remove:
            break
        for r, c in to_remove:
            rolls[r][c] = '.'
    return total


def _is_free_to_remove(rolls, row, col, w, h) -> bool:
    count = 0
    for y, x in neighbors8(row, col):
        if not in_bounds(y, x, h, w):
            continue
        if get(rolls, y, x) == '@':
            count += 1
            if count >= 4:
                return False
    return True


if __name__ == "__main__":
    from aoc.runner import run_day_from_file

    run_day_from_file(__file__, globals())
