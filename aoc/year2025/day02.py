"""Advent of Code 2025 - Day 02: Gift Shop."""


def parse(raw: str):
    ranges = []
    for part in raw.split(','):
        ranges.append(map(int, part.split('-')))
    return ranges


def solve_part1(raw: str):
    total = 0
    for start, end in parse(raw):
        for n in range(start, end + 1):
            s = str(n)
            if len(s) % 2 == 0 and s[:len(s)//2] == s[len(s)//2:]:
                total += n
    return total


def solve_part2(raw: str):
    total = 0
    for start, end in parse(raw):
        total += sum(n for n in range(start, end + 1) if _is_repeated(str(n)))
    return total


def _is_repeated(s: str) -> bool:
    """
    Return True if s is composed of a smaller substring repeated ≥ 2 times.

    This uses the classic trick: take the string doubled (s + s), remove the first and last characters ([1:-1]),
    and check whether the original string appears in that slice.
    """
    return len(s) > 1 and s in (s + s)[1:-1]



if __name__ == "__main__":
    from aoc.runner import run_day_from_file

    run_day_from_file(__file__, globals())
