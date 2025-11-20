from aoc.year2024 import day04


EXAMPLE_INPUT = """\
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


def test_parse_example():
    data = day04.parse(EXAMPLE_INPUT)
    assert isinstance(data, list)


def test_part1_example():
    result = day04.solve_part1(EXAMPLE_INPUT)
    assert result == 18


def test_part2_example():
    result = day04.solve_part2(EXAMPLE_INPUT)
    assert result == 9
