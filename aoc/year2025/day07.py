"""Advent of Code 2025 - Day 07: Laboratories."""
from collections import defaultdict

from aoc.utils.grid import parse_grid

def parse(raw: str):
    return parse_grid(raw)


def solve_part1(raw: str):
    grid = parse(raw)
    beams = {grid[0].index('S')}
    splits = 0

    for next_row in grid[1:]:
        # beams that hit a splitter in the next row
        split_beams = {b for b in beams if next_row[b] == '^'}
        splits += len(split_beams)

        # beams that continue straight in the next row
        straight_beams = {b for b in beams if next_row[b] != '^'}

        # split beams produce left and right beams; include straight beams unchanged
        beams = {b - 1 for b in split_beams} | {b + 1 for b in split_beams} | straight_beams

    return splits


def solve_part2(raw: str):
    grid = parse(raw)
    beams = defaultdict(int)
    beams[grid[0].index("S")] = 1

    for row in grid[1:]:
        # collect indices where a splitter '^' has an incoming beam
        splits = [i for i, cell in enumerate(row) if cell == "^" and beams[i] > 0]

        # apply splitting: move counts left/right and clear the splitter cell
        for s in splits:
            cnt = beams[s]
            beams[s - 1] += cnt
            beams[s + 1] += cnt
            beams[s] = 0

    return sum(beams.values())


if __name__ == "__main__":
    from aoc.runner import run_day_from_file

    run_day_from_file(__file__, globals())
