from aoc.year2024 import day06


EXAMPLE_INPUT = """\
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
"""


def test_parse_example():
    data = day06.parse(EXAMPLE_INPUT)
    assert isinstance(data, (list, tuple, str))


def test_part1_example():
    result = day06.solve_part1(EXAMPLE_INPUT)
    assert result == 41


def test_part2_example():
    result = day06.solve_part2(EXAMPLE_INPUT)
    assert result == 6
