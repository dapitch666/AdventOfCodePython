from aoc.year2025 import day01


EXAMPLE_INPUT = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""


def test_parse_example():
    data = day01.parse(EXAMPLE_INPUT)
    # TODO: adjust expected structure
    assert isinstance(data, list)


def test_part1_example():
    result = day01.solve_part1(EXAMPLE_INPUT)
    assert result == 3


def test_part2_example():
    result = day01.solve_part2(EXAMPLE_INPUT)
    assert result == 6
