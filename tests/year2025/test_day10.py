from aoc.year2025 import day10


EXAMPLE_INPUT = """\
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""


def test_parse_example():
    data = day10.parse(EXAMPLE_INPUT)
    assert isinstance(data, (list, tuple, str))


def test_part1_example():
    result = day10.solve_part1(EXAMPLE_INPUT)
    assert result == 7


def test_part2_example():
    result = day10.solve_part2(EXAMPLE_INPUT)
    assert result == 33
