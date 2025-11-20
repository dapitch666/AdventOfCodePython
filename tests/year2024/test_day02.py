from aoc.year2024 import day02


EXAMPLE_INPUT = """\
7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


def test_parse_example():
    data = day02.parse(EXAMPLE_INPUT)
    assert isinstance(data, list)


def test_part1_example():
    result = day02.solve_part1(EXAMPLE_INPUT)
    assert result == 2


def test_part2_example():
    result = day02.solve_part2(EXAMPLE_INPUT)
    assert result == 4
