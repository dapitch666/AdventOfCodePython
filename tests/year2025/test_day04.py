from aoc.year2025 import day04


EXAMPLE_INPUT = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""


def test_parse_example():
    data = day04.parse(EXAMPLE_INPUT)
    assert isinstance(data, list)


def test_part1_example():
    result = day04.solve_part1(EXAMPLE_INPUT)
    assert result == 13


def test_part2_example():
    result = day04.solve_part2(EXAMPLE_INPUT)
    assert result == 43
