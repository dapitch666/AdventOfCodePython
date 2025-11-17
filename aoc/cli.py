import argparse
import re
from datetime import date
from importlib import import_module
from typing import Optional

from .io import load_input


def extract_title_from_module(module) -> Optional[str]:
    """Extract the AoC puzzle title from the module's docstring, if present.

    Expects something like:
    \"\"\"Advent of Code 2025 - Day 01: Historian Hysteria.\"\"\"
    """
    doc = module.__doc__ or ""
    first_line = doc.strip().splitlines()[0].strip() if doc.strip() else ""
    if not first_line:
        return None

    # Try to match the pattern and capture the title part.
    match = re.search(r"Advent of Code \d{4} - Day \d{2}: (.+)", first_line)
    if not match:
        return None

    title = match.group(1).strip()
    # Remove trailing period if present (common in AoC titles).
    if title.endswith("."):
        title = title[:-1]
    return title or None


def run_day(year: int, day: int) -> None:
    module_name = f"aoc.year{year}.day{day:02d}"
    try:
        module = import_module(module_name)
    except ModuleNotFoundError:
        print(f"[WARN] No module for year={year}, day={day:02d}")
        return

    raw = load_input(year, day)
    if not raw:
        print(f"[WARN] No input found for {year} day {day:02d}")
        return

    part1 = getattr(module, "solve_part1", None)
    part2 = getattr(module, "solve_part2", None)

    title = extract_title_from_module(module)
    if title:
        header = f"=== {year} Day {day:02d}: {title} ==="
    else:
        header = f"=== {year} Day {day:02d} ==="

    print(header)
    if part1:
        print("Part 1:", part1(raw))
    else:
        print("Part 1: (solve_part1 not implemented)")
    if part2:
        print("Part 2:", part2(raw))
    else:
        print("Part 2: (solve_part2 not implemented)")


def run_year(year: int, max_day: int = 25) -> None:
    for day in range(1, max_day + 1):
        run_day(year, day)
        print()


def infer_december_day() -> tuple[int | None, int | None]:
    """
    If today is between Dec 1st and Dec 25th (inclusive), return (year, day).
    Otherwise, return (None, None).
    """
    today = date.today()
    if today.month == 12 and 1 <= today.day <= 25:
        return today.year, today.day
    return None, None


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="aoc",
        description="Advent of Code runner",
    )
    parser.add_argument("year", type=int, nargs="?", help="Year (e.g. 2025)")
    parser.add_argument("day", type=int, nargs="?", help="Day (1-25)")
    parser.add_argument(
        "--all",
        action="store_true",
        help="Run all days for the given year",
    )

    args = parser.parse_args()

    # Case 1: no args at all → try to auto-run today's puzzle in December
    if args.year is None and args.day is None and not args.all:
        year, day = infer_december_day()
        if year is not None and day is not None:
            print(
                f"[INFO] No arguments provided, running today's puzzle: "
                f"year={year}, day={day:02d}"
            )
            run_day(year, day)
            return

        parser.error(
            "You must provide a year (and optionally a day), except between "
            "December 1 and 25 where the current day is used by default."
        )

    # Case 2: --all must have a year
    if args.all:
        if args.year is None:
            parser.error("You must provide a year when using --all.")
        run_year(args.year)
        return

    # Case 3: run a specific day
    if args.year is None or args.day is None:
        parser.error("You must provide both year and day, or use --all.")

    run_day(args.year, args.day)
