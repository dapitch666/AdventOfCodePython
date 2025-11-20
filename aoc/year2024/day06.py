"""Advent of Code 2024 - Day 06: Guard Gallivant."""

from collections import defaultdict
from bisect import bisect, insort
from typing import Dict, List, Tuple

from aoc.utils.grid import parse_grid, in_bounds, step, DIRECTIONS_4

DIR_UP, DIR_RIGHT, DIR_DOWN, DIR_LEFT = range(4)


def parse(raw: str) -> Tuple[List[str], Tuple[int, int]]:
    grid = parse_grid(raw)
    for y, row in enumerate(grid):
        if "^" in row:
            return grid, (y, row.index("^"))
    raise ValueError("No '^' found.")


def solve_part1(raw: str) -> int:
    grid, (y, x) = parse(raw)
    return len(get_path(grid, y, x))


def get_path(grid: List[str], start_y: int, start_x: int) -> set[Tuple[int, int]]:
    h, w = len(grid), len(grid[0])
    y, x = start_y, start_x
    visited = {(y, x)}
    d = DIR_UP

    while True:
        dy, dx = DIRECTIONS_4[d]
        next_y, next_x = step(y, x, dy, dx)

        if not in_bounds(next_y, next_x, h, w):
            return visited

        if grid[next_y][next_x] != "#":
            y, x = next_y, next_x
            visited.add((y, x))
        else:
            d = (d + 1) % 4


def build_obstacle_index(grid: List[str]) -> Tuple[Dict[int, List[int]], Dict[int, List[int]]]:
    """
    Return (rows, cols) where:
      rows[r] = sorted list of columns with obstacles on row r
      cols[c] = sorted list of rows with obstacles on column c
    """
    rows: Dict[int, List[int]] = defaultdict(list)
    cols: Dict[int, List[int]] = defaultdict(list)

    for y, row in enumerate(grid):
        for x, ch in enumerate(row):
            if ch == "#":
                rows[y].append(x)
                cols[x].append(y)

    for lst in rows.values():
        lst.sort()
    for lst in cols.values():
        lst.sort()

    return rows, cols


def _prev(sorted_list: List[int], value: int):
    """Return largest element < value or None."""
    i = bisect(sorted_list, value)
    return sorted_list[i - 1] if i > 0 else None


def _next(sorted_list: List[int], value: int):
    """Return smallest element > value or None."""
    i = bisect(sorted_list, value)
    return sorted_list[i] if i < len(sorted_list) else None


def move_with_index(
    y: int,
    x: int,
    d: int,
    rows: Dict[int, List[int]],
    cols: Dict[int, List[int]],
    h: int,
    w: int,
) -> Tuple[int, int, int]:
    """
    Move from (y,x) in direction d to just before the next obstacle (or outside).
    Return (new_y, new_x, new_direction) where direction is rotated right.
    """
    if d == DIR_UP:
        prev_row = _prev(cols.get(x, []), y)
        new_y = (prev_row + 1) if prev_row is not None else -1
        return new_y, x, DIR_RIGHT

    if d == DIR_RIGHT:
        next_col = _next(rows.get(y, []), x)
        new_x = (next_col - 1) if next_col is not None else w
        return y, new_x, DIR_DOWN

    if d == DIR_DOWN:
        next_row = _next(cols.get(x, []), y)
        new_y = (next_row - 1) if next_row is not None else h
        return new_y, x, DIR_LEFT

    # DIR_LEFT
    prev_col = _prev(rows.get(y, []), x)
    new_x = (prev_col + 1) if prev_col is not None else -1
    return y, new_x, DIR_UP


def is_looping(
    start_y: int,
    start_x: int,
    rows: Dict[int, List[int]],
    cols: Dict[int, List[int]],
    h: int,
    w: int,
) -> bool:
    y, x, d = start_y, start_x, DIR_UP
    seen = {(y, x, d)}
    while 0 <= y < h and 0 <= x < w:
        y, x, d = move_with_index(y, x, d, rows, cols, h, w)
        state = (y, x, d)
        if state in seen:
            return True
        seen.add(state)
    return False


def solve_part2(raw: str) -> int:
    grid, (start_y, start_x) = parse(raw)
    h, w = len(grid), len(grid[0])
    rows, cols = build_obstacle_index(grid)

    candidates: set[Tuple[int, int]] = set()
    y, x, d = start_y, start_x, DIR_UP

    while 0 <= y < h and 0 <= x < w:
        new_y, new_x, new_d = move_with_index(y, x, d, rows, cols, h, w)

        if d == DIR_UP:
            for yy in range(new_y + 1, y + 1):
                candidates.add((yy, x))
        elif d == DIR_RIGHT:
            for xx in range(x, new_x + 1):
                candidates.add((y, xx))
        elif d == DIR_DOWN:
            for yy in range(y, new_y + 1):
                candidates.add((yy, x))
        else:  # DIR_LEFT
            for xx in range(new_x + 1, x + 1):
                candidates.add((y, xx))

        y, x, d = new_y, new_x, new_d

    candidates.discard((start_y, start_x))

    loop_count = 0
    for oy, ox in list(candidates):
        insort(rows[oy], ox)
        insort(cols[ox], oy)

        if is_looping(start_y, start_x, rows, cols, h, w):
            loop_count += 1

        rows[oy].remove(ox)
        cols[ox].remove(oy)

    return loop_count


if __name__ == "__main__":
    from aoc.runner import run_day_from_file

    run_day_from_file(__file__, globals())