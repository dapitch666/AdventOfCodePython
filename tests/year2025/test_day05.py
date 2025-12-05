from aoc.year2025 import day05


EXAMPLE_INPUT = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""


def test_parse_example():
    rules, available = day05.parse(EXAMPLE_INPUT)
    assert isinstance(rules, tuple)
    assert isinstance(available, list)


def test_part1_example():
    result = day05.solve_part1(EXAMPLE_INPUT)
    assert result == 3


def test_part2_example():
    result = day05.solve_part2(EXAMPLE_INPUT)
    assert result == 14
