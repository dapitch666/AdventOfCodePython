from aoc.year2024 import day05


EXAMPLE_INPUT = """\
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


def test_parse_example():
    rules, updates = day05.parse(EXAMPLE_INPUT)
    assert isinstance(rules, list)
    assert isinstance(updates, list)


def test_part1_example():
    result = day05.solve_part1(EXAMPLE_INPUT)
    assert result == 143


def test_part2_example():
    result = day05.solve_part2(EXAMPLE_INPUT)
    assert result == 123
