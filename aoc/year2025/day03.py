"""Advent of Code 2025 - Day 03: Lobby."""


def parse(raw: str) -> tuple[list[str], int]:
    banks = raw.splitlines()
    return banks, len(banks[0])


def solve_part1(raw: str):
    data, l = parse(raw)
    total_joltage = 0
    for line in data:
        # find index of the maximum digit in line[0:-1] (first occurrence on ties)
        largest_idx = max(range(l - 1), key=line.__getitem__)
        largest = line[largest_idx]
        # find maximum digit in the remainder of the line after largest_idx
        largest2 = max(line[largest_idx + 1 :])
        total_joltage += int(largest) * 10 + int(largest2)
    return total_joltage


def solve_part2(raw: str):
    data, l = parse(raw)
    total_joltage = 0
    for line in data:
        idx = 0
        digits = []
        for i in range(12, 0, -1):
            idx = max(range(idx, l - i + 1), key=line.__getitem__)
            digits.append(line[idx])
            idx += 1

        total_joltage += int("".join(digits))

    return total_joltage

if __name__ == "__main__":
    from aoc.runner import run_day_from_file

    run_day_from_file(__file__, globals())
