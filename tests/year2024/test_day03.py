from aoc.year2024 import day03


EXAMPLE_INPUT = """\
xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
"""


def test_parse_example():
    data = day03.parse(EXAMPLE_INPUT)
    assert isinstance(data, str)


def test_part1_example():
    result = day03.solve_part1(EXAMPLE_INPUT)
    assert result == 161


def test_part2_example():
    result = day03.solve_part2("xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))")
    assert result == 48
