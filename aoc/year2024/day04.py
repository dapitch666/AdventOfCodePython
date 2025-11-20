"""Advent of Code 2024 - Day 04: Ceres Search."""

from aoc.utils.grid import DIRECTIONS_8, parse_grid, in_bounds, step

def parse(raw: str):
    return parse_grid(raw)


def solve_part1(raw: str):
    grid = parse(raw)
    h, w = len(grid), len(grid[0])

    return sum(
        1
        for y in range(h)
        for x in range(w)
        for dy, dx in DIRECTIONS_8
        if matches_xmas(grid, y, x, dy, dx)
    )


def solve_part2(raw: str):
    grid = parse(raw)
    h, w = len(grid), len(grid[0])

    return sum(
        1
        for y in range(1, h - 1)
        for x in range(1, w - 1)
        if matches_x_mas(grid, y, x)
    )


def matches_xmas(grid, y, x, dy, dx):
    if not grid[y][x] == 'X':
        return False

    h, w = len(grid), len(grid[0])
    end_y, end_x = step(y, x, dy, dx, 3)

    if not in_bounds(end_y, end_x, h, w):
        return False

    for k, ch in enumerate("XMAS"):
        yy, xx = step(y, x, dy, dx, k)
        if grid[yy][xx] != ch:
            return False
    return True


def matches_x_mas(grid, y, x):
    if not grid[y][x] == 'A':
        return False

    d1 = grid[y - 1][x - 1] + grid[y + 1][x + 1]
    d2 = grid[y - 1][x + 1] + grid[y + 1][x - 1]

    return d1 in ("MS", "SM") and d2 in ("MS", "SM")


if __name__ == "__main__":
    from aoc.runner import run_day_from_file

    run_day_from_file(__file__, globals())
