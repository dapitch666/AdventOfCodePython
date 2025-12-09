"""Advent of Code 2025 - Day 09: Movie Theater."""
from itertools import combinations
from bisect import bisect_left, bisect_right
from typing import List, Tuple, Dict


def parse(raw: str) -> list[tuple[int, ...]]:
    return [tuple(map(int, line.split(','))) for line in raw.splitlines() if line.strip()]


def rect(a, b) -> Tuple[int, int, int, int]:
    (x1, y1), (x2, y2) = a, b
    return min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)


def rects_overlap(r, s):
    rxmin, rxmax, rymin, rymax = r
    sxmin, sxmax, symin, symax = s
    return rxmin < sxmax and rxmax > sxmin and rymin < symax and rymax > symin


def build_segments(reds: List[Tuple[int, ...]]):
    """Return lists/dicts of vertical and horizontal segments as inclusive bounding boxes:
       vertical: (x, y1, y2) with y1 <= y2
       horizontal: (y, x1, x2) with x1 <= x2
    """
    n = len(reds)
    verticals = []    # tuples (x, y1, y2)
    horizontals = []  # tuples (y, x1, x2)
    for i in range(n):
        x1, y1 = reds[i]
        x2, y2 = reds[(i + 1) % n]
        if x1 == x2:
            a, b = sorted((y1, y2))
            verticals.append((x1, a, b))
        elif y1 == y2:
            a, b = sorted((x1, x2))
            horizontals.append((y1, a, b))

    return verticals, horizontals


def index_segments(verticals, horizontals):
    """Build dicts:
       v_by_x: x -> list of (y1,y2)
       h_by_y: y -> list of (x1,x2)
       and sorted lists of keys for bisect.
    """
    v_by_x: Dict[int, List[Tuple[int,int]]] = {}
    for x, y1, y2 in verticals:
        v_by_x.setdefault(x, []).append((y1,y2))
    h_by_y: Dict[int, List[Tuple[int,int]]] = {}
    for y, x1, x2 in horizontals:
        h_by_y.setdefault(y, []).append((x1,x2))

    v_x_keys = sorted(v_by_x.keys())
    h_y_keys = sorted(h_by_y.keys())
    return v_by_x, v_x_keys, h_by_y, h_y_keys


def any_segment_overlaps_rectangle(rect, v_by_x, v_x_keys, h_by_y, h_y_keys):
    """Return True if any segment (vertical or horizontal) overlaps rect according to rects_overlap semantics."""
    xmin, xmax, ymin, ymax = rect

    # candidate verticals: x such that xmin < x < xmax
    li = bisect_right(v_x_keys, xmin)
    ri = bisect_left(v_x_keys, xmax)
    if li < ri:
        # there are vertical keys with xmin < x < xmax
        for x in v_x_keys[li:ri]:
            for (y1,y2) in v_by_x[x]:
                # segment box: x..x, y1..y2
                # overlap test simplified for vertical:
                # check if rect.ymin < y2 and rect.ymax > y1 (and x in between already ensured)
                if ymin < y2 and ymax > y1:
                    return True

    # candidate horizontals: y such that ymin < y < ymax
    li = bisect_right(h_y_keys, ymin)
    ri = bisect_left(h_y_keys, ymax)
    if li < ri:
        for y in h_y_keys[li:ri]:
            for (x1,x2) in h_by_y[y]:
                # segment box: x1..x2, y..y
                # check if rect.xmin < x2 and rect.xmax > x1
                if xmin < x2 and xmax > x1:
                    return True

    return False


def solve_part1(raw: str):
    reds = parse(raw)
    best = 0
    # iterate pairs
    for a, b in combinations(reds, 2):
        area = abs(a[0] - b[0] + 1) * abs(a[1] - b[1] + 1)
        if area > best:
            best = area
    return best


def solve_part2(raw: str):
    reds = parse(raw)
    n = len(reds)
    # prebuild all rectangles as (xmin, xmax, ymin, ymax)
    rects = [rect(reds[i], reds[j]) for i in range(n - 1) for j in range(i + 1, n)]

    # build segments (lines) between consecutive reds (wrap)
    verticals, horizontals = build_segments(reds)
    v_by_x, v_x_keys, h_by_y, h_y_keys = index_segments(verticals, horizontals)

    # filter rectangles that do NOT overlap any segment
    best = 0
    for r in rects:
        # quick bounding-box early prune: if potential area <= best2 skip
        area = (r[1] - r[0] + 1) * (r[3] - r[2] + 1)
        if area <= best:
            continue
        if not any_segment_overlaps_rectangle(r, v_by_x, v_x_keys, h_by_y, h_y_keys):
            best = area

    return best


if __name__ == "__main__":
    from aoc.runner import run_day_from_file

    run_day_from_file(__file__, globals())