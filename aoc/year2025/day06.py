"""Advent of Code 2025 - Day 06: Trash Compactor."""
from typing import List, Tuple
import math


def parse(raw: str) -> Tuple[List[List[str]], List[str]]:
    """
    Return a list of problem chunks (each chunk is a list of the number-rows as strings)
    and a parallel list of operation characters (one per chunk).
    """
    lines = raw.splitlines()
    max_len = max(len(l) for l in lines)
    lines = [l.ljust(max_len) for l in lines]

    # determine which columns are completely blank
    is_blank_col = [all(line[col] == " " for line in lines) for col in range(max_len)]

    # find contiguous ranges of non-blank columns (each is one problem)
    blocks: List[Tuple[int, int]] = []
    i = 0
    while i < max_len:
        if not is_blank_col[i]:
            start = i
            while i < max_len and not is_blank_col[i]:
                i += 1
            blocks.append((start, i))
        else:
            i += 1

    chunks: List[List[str]] = []
    ops: List[str] = []
    for start, end in blocks:
        chunk_rows = [line[start:end] for line in lines]
        op_row = chunk_rows[-1]
        op = next((c for c in op_row if c != " "), "")
        if op:
            # store only the number-rows (all rows except the last/op row)
            chunks.append(chunk_rows[:-1])
            ops.append(op)

    return chunks, ops


def compute(op: str, nums: List[int]) -> int:
    if op == "+":
        return sum(nums)
    else:
        return math.prod(nums)


def solve_part1(raw: str):
    """
    Interpret each problem horizontally: each row (except the op row) is a whole number.
    """
    chunks, ops = parse(raw)
    total = 0
    for chunk_rows, op in zip(chunks, ops):
        nums = [int(r.strip()) for r in chunk_rows if r.strip()]
        total += compute(op, nums)
    return total


def solve_part2(raw: str):
    """
    Interpret each problem as column-wise numbers read right-to-left (each column is a number).
    """
    chunks, ops = parse(raw)
    total = 0
    for chunk_rows, op in zip(chunks, ops):
        width = len(chunk_rows[0])
        nums: List[int] = []
        # read columns right-to-left; each column's chars top->bottom form a number
        for col in range(width - 1, -1, -1):
            col_chars = [row[col] for row in chunk_rows]
            nums.append(int("".join(col_chars).strip()))
        total += compute(op, nums)
    return total


if __name__ == "__main__":
    from aoc.runner import run_day_from_file

    run_day_from_file(__file__, globals())
