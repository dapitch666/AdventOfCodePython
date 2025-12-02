from aoc.year2025 import day02


EXAMPLE_INPUT = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"


def test_parse_example():
    data = day02.parse(EXAMPLE_INPUT)
    assert isinstance(data, list)


def test_part1_example():
    result = day02.solve_part1(EXAMPLE_INPUT)
    assert result == 1227775554


def test_part2_example():
    result = day02.solve_part2(EXAMPLE_INPUT)
    assert result == 4174379265
