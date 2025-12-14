"""Advent of Code 2025 - Day 11: Reactor."""

from collections import defaultdict


def parse(raw: str):
    connections = defaultdict(set)
    for line in raw.splitlines():
        src, dsts = line.split(": ")
        connections[src].update(dsts.split())
    return connections


def count_paths(conns, start, init, step, accept):
    """Count paths from start to node 'out' using a DFS with memoization.

        - `connections` maps a node to its outgoing nodes.
        - `start` is the starting node name.
        - `init` is the initial traversal state passed into `dfs`.
        - `step(node, state)` returns the updated state after visiting `node`.
        - `accept(state)` returns True when a path ending at 'out' should be counted.
        """
    memo = {}

    def dfs(node, state):
        key = (node, state)
        if key in memo:
            return memo[key]

        if node == "out":
            res = 1 if accept(state) else 0
            memo[key] = res
            return res

        total = 0
        for nxt in conns.get(node, ()):
            total += dfs(nxt, step(nxt, state))

        memo[key] = total
        return total

    return dfs(start, init)


def solve_part1(raw: str):
    return count_paths(
        conns=parse(raw),
        start="you",
        init=None,
        step=lambda _, s: s,    # state is unused for part 1
        accept=lambda _: True,  # accept every path that reaches 'out'
    )


def solve_part2(raw: str):
    return count_paths(
        conns=parse(raw),
        start="svr",
        init=(False, False),
        step=lambda node, state: (state[0] or node == "fft", state[1] or node == "dac"),
        accept=lambda state: state[0] and state[1],
    )


if __name__ == "__main__":
    from aoc.runner import run_day_from_file
    run_day_from_file(__file__, globals())
