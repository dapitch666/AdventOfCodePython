from aoc.year2025 import day06


EXAMPLE_INPUT = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +
"""


def test_parse_example():
    data = day06.parse(EXAMPLE_INPUT)
    assert isinstance(data, (list, tuple, str))


def test_part1_example():
    result = day06.solve_part1(EXAMPLE_INPUT)
    assert result == 4277556


def test_part2_example():
    result = day06.solve_part2(EXAMPLE_INPUT)
    assert result == 3263827
