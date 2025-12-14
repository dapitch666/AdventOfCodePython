from aoc.year2025 import day11


EXAMPLE_INPUT = """\
aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out
"""

EXAMPLE_INPUT_2 = """\
svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
"""


def test_parse_example():
    data = day11.parse(EXAMPLE_INPUT)
    assert isinstance(data, (list, tuple, str))


def test_part1_example():
    result = day11.solve_part1(EXAMPLE_INPUT)
    assert result == 5


def test_part2_example():
    result = day11.solve_part2(EXAMPLE_INPUT_2)
    assert result == 2
