"""Advent of Code 2025 - Day 08: Playground."""
import heapq
from math import prod
from typing import List, Tuple
from collections import Counter
from itertools import combinations


def parse(raw: str) -> List[Tuple[int, ...]]:
    return [tuple(map(int, line.split(','))) for line in raw.splitlines()]


class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        # path compression
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def union(self, a: int, b: int) -> bool:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return False
        # union by size
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        return True

    def component_sizes(self) -> List[int]:
        counts = Counter(self.find(i) for i in range(len(self.parent)))
        return sorted(counts.values(), reverse=True)


def dist2(p1: Tuple[int, ...], p2: Tuple[int, ...]) -> int:
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2 + (p1[2] - p2[2]) ** 2


def solve_part1(raw: str, n: int = 1000) -> int:
    points = parse(raw)

    # build all pair distances and pick the k smallest
    edges = ((dist2(p1, p2), i, j) for (i, p1), (j, p2) in combinations(enumerate(points), 2))
    smallest = heapq.nsmallest(n, edges, key=lambda x: x[0])

    # sort ascending by distance and union in that order
    smallest.sort(key=lambda x: x[0])
    dsu = DSU(len(points))
    for _, i, j in smallest:
        dsu.union(i, j)

    sizes = dsu.component_sizes()
    return prod(sizes[:3])


def solve_part2(raw: str):
    points = parse(raw)
    n = len(points)
    INF = 10**30
    key = [INF] * n
    parent = [-1] * n
    in_mst = [False] * n

    key[0] = 0
    max_edge = (-1, -1, -1)  # (weight, u, v)

    for _ in range(n):
        # pick the not-in-mst vertex with minimal key
        u = min((key[i], i) for i in range(n) if not in_mst[i])[1]
        in_mst[u] = True

        # if u has a parent, we added edge (parent[u], u) with weight key[u]
        if parent[u] != -1:
            w = key[u]
            # update max edge if necessary
            if w > max_edge[0]:
                max_edge = (w, parent[u], u)

        # update keys for vertices not yet in MST
        pu = points[u]
        for v in range(n):
            if in_mst[v]:
                continue
            d = dist2(pu, points[v])
            if d < key[v]:
                key[v] = d
                parent[v] = u

    _, u, v = max_edge
    return points[u][0] * points[v][0]


if __name__ == "__main__":
    from aoc.runner import run_day_from_file

    run_day_from_file(__file__, globals())
