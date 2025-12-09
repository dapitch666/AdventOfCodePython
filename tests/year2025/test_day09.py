from aoc.year2025 import day09


EXAMPLE_INPUT = """\
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""


def test_parse_example():
    data = day09.parse(EXAMPLE_INPUT)
    assert isinstance(data, list)


def test_part1_example():
    result = day09.solve_part1(EXAMPLE_INPUT)
    assert result == 50


def test_part2_example():
    result = day09.solve_part2(EXAMPLE_INPUT)
    assert result == 24
