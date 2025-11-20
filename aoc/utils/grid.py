"""
Utility functions for 2D grids used in Advent of Code puzzles.
"""

from __future__ import annotations
from typing import Iterable, Tuple, List


# Common direction vectors (dy, dx)
DIRECTIONS_4 = [
    (-1, 0),  # up
    (0, 1),   # right
    (1, 0),   # down
    (0, -1),  # left
]

DIRECTIONS_8 = [
    (-1, 0),  # up
    (1, 0),   # down
    (0, -1),  # left
    (0, 1),   # right
    (-1, -1), # up-left
    (-1, 1),  # up-right
    (1, -1),  # down-left
    (1, 1),   # down-right
]

DIAGONALS = [
    (-1, -1), # up-left
    (-1, 1),  # up-right
    (1, -1),  # down-left
    (1, 1),   # down-right
]


def in_bounds(y: int, x: int, height: int, width: int) -> bool:
    """Return True if (y, x) is inside a grid of size height × width."""
    return 0 <= y < height and 0 <= x < width


def parse_grid(raw: str) -> List[str]:
    """Parse a multi-line string into a rectangular grid (list of strings)."""
    return [line.rstrip("\n") for line in raw.splitlines() if line]


def get(grid: List[str], y: int, x: int) -> str:
    """Get the character at (y, x) without needing grid[y][x] everywhere."""
    return grid[y][x]


def neighbors4(y: int, x: int) -> Iterable[Tuple[int, int]]:
    """Yield the 4 orthogonal neighbors around (y, x)."""
    for dy, dx in DIRECTIONS_4:
        yield y + dy, x + dx


def neighbors8(y: int, x: int) -> Iterable[Tuple[int, int]]:
    """Yield the 8 neighbors around (y, x)."""
    for dy, dx in DIRECTIONS_8:
        yield y + dy, x + dx


def step(y: int, x: int, dy: int, dx: int, steps: int = 1) -> Tuple[int, int]:
    """
    Move (y, x) by steps × (dy, dx).
    Useful for walking in a direction.
    """
    return y + dy * steps, x + dx * steps
