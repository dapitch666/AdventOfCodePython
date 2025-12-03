from aoc.year2025 import day03


EXAMPLE_INPUT = """\
987654321111111
811111111111119
234234234234278
818181911112111
"""


def test_parse_example():
    data = day03.parse(EXAMPLE_INPUT)
    assert isinstance(data, tuple)


def test_part1_example():
    result = day03.solve_part1(EXAMPLE_INPUT)
    assert result == 357


def test_part2_example():
    result = day03.solve_part2(EXAMPLE_INPUT)
    assert result == 3121910778619
