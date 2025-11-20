from aoc.year2024 import day01


EXAMPLE_INPUT = """\
3   4
4   3
2   5
1   3
3   9
3   3
"""


def test_parse_example():
    data = day01.parse(EXAMPLE_INPUT)
    assert isinstance(data, tuple)


def test_part1_example():
    result = day01.solve_part1(EXAMPLE_INPUT)
    assert result == 11


def test_part2_example():
    result = day01.solve_part2(EXAMPLE_INPUT)
    # TODO: replace with the expected value from the problem example
    assert result == 31
