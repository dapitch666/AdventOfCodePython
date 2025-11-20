"""Advent of Code 2024 - Day 05: Print Queue."""


def parse(raw: str) -> tuple[list[tuple[int, int]], list[list[int]]]:
    rules_block, updates_block = raw.strip().split("\n\n")

    rules: list[tuple[int, int]] = [
        (int(a), int(b))
        for a, b in (line.split("|") for line in rules_block.splitlines())
    ]
    updates = [list(map(int, line.split(","))) for line in updates_block.splitlines()]

    return rules, updates


def solve_part1(raw: str):
    rules, updates = parse(raw)
    total = 0
    for update in updates:
        if is_valid_update(update, rules):
            total += score(update)
    return total


def score(update: list[int]) -> int:
    return update[len(update) // 2]


def solve_part2(raw: str):
    rules, updates = parse(raw)
    total = 0
    for update in updates:
        if not is_valid_update(update, rules):
            fixed = fix_update(update, rules)
            if fixed is not None:
                total += score(fixed)
    return total


def is_valid_update(update: list[int], rules: list[tuple[int, ...]]) -> bool:
    pos = {value: idx for idx, value in enumerate(update)}
    for before, after in rules:
        if before in pos and after in pos:
            # Rule applies: before must come before after
            if pos[before] > pos[after]:
                return False

    return True


def fix_update(update, rules):
    pos = {value: idx for idx, value in enumerate(update)}

    for before, after in rules:
        if before in pos and after in pos and pos[before] > pos[after]:
            # Rule is violated → swap the two pages and recurse
            i, j = pos[before], pos[after]
            new_update = update.copy()
            new_update[i], new_update[j] = new_update[j], new_update[i]
            return fix_update(new_update, rules)

    # If we get here, no rule is violated anymore → the update is fixed
    return update


if __name__ == "__main__":
    from aoc.runner import run_day_from_file

    run_day_from_file(__file__, globals())
