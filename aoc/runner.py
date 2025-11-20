from __future__ import annotations

from pathlib import Path
import time
import re
from typing import Any, Dict, List, Tuple

from .io import load_input


_TITLE_RE = re.compile(r"Advent of Code \d{4} - Day \d{2}: (.+)")


def _extract_title(doc: str) -> str | None:
    """Extract the puzzle title from the module docstring, if present."""
    if not doc:
        return None
    first_line = doc.strip().splitlines()[0].strip()
    match = _TITLE_RE.search(first_line)
    if not match:
        return None
    title = match.group(1).strip()
    if title.endswith("."):
        title = title[:-1]
    return title or None


def _format_duration(seconds: float) -> str:
    """Format a duration in a human-friendly way."""
    if seconds < 1e-6:
        return f"{seconds * 1e9:.1f} ns"
    if seconds < 1e-3:
        return f"{seconds * 1e6:.1f} µs"
    if seconds < 1:
        return f"{seconds * 1e3:.1f} ms"
    return f"{seconds:.3f} s"


def _print_table(rows: List[Tuple[str, str, str]]) -> None:
    """Print a simple ASCII table: (label, value, time)."""
    if not rows:
        return

    headers = ("Part", "Answer", "Time")
    widths = [
        max(len(headers[0]), max(len(row[0]) for row in rows)),
        max(len(headers[1]), max(len(row[1]) for row in rows)),
        max(len(headers[2]), max(len(row[2]) for row in rows)),
    ]

    def make_border() -> str:
        return "+" + "+".join("-" * (w + 2) for w in widths) + "+"

    def format_row(cols: Tuple[str, str, str]) -> str:
        return "| " + " | ".join(col.ljust(w) for col, w in zip(cols, widths)) + " |"

    border = make_border()
    print(border)
    print(format_row(headers))
    print(border)
    for row in rows:
        print(format_row(row))
    print(border)


def run_day_from_file(file: str, module_globals: Dict[str, Any]) -> None:
    """
    Run a day module based on its file path.

    Intended usage (inside dayXX.py):

        if __name__ == "__main__":
            from aoc.runner import run_day_from_file
            run_day_from_file(__file__, globals())
    """
    path = Path(file).resolve()
    year = int(path.parent.name.replace("year", ""))
    day = int(path.stem.replace("day", ""))

    raw = load_input(year, day)

    solve_part1 = module_globals.get("solve_part1")
    solve_part2 = module_globals.get("solve_part2")
    doc = module_globals.get("__doc__", "") or ""
    title = _extract_title(doc)

    if title:
        header = f"=== {year} Day {day:02d}: {title} ==="
    else:
        header = f"=== {year} Day {day:02d} ==="
    print(header)

    rows: List[Tuple[str, str, str]] = []

    if callable(solve_part1):
        t0 = time.perf_counter()
        try:
            result = solve_part1(raw)
        except Exception as exc:  # pragma: no cover (debug aid)
            result = f"ERROR: {exc}"
        dt = time.perf_counter() - t0
        rows.append(("Part 1", str(result), _format_duration(dt)))

    if callable(solve_part2):
        t0 = time.perf_counter()
        try:
            result = solve_part2(raw)
        except Exception as exc:  # pragma: no cover (debug aid)
            result = f"ERROR: {exc}"
        dt = time.perf_counter() - t0
        rows.append(("Part 2", str(result), _format_duration(dt)))

    _print_table(rows)
