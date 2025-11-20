#!/usr/bin/env python3
import sys
import re
from datetime import date
from pathlib import Path
from textwrap import dedent
from typing import Tuple

import requests
from bs4 import BeautifulSoup


PROJECT_ROOT = Path(__file__).resolve().parents[1]
AOC_PACKAGE = PROJECT_ROOT / "aoc"
TESTS_ROOT = PROJECT_ROOT / "tests"


DAY_TEMPLATE = """\
\"\"\"Advent of Code {year} - Day {day:02d}{title_suffix}.\"\"\"


def parse(raw: str):
    \"\"\"Parse the raw input.

    Adapt this function to the actual problem statement.
    \"\"\"
    return raw.splitlines()


def solve_part1(raw: str):
    data = parse(raw)
    # TODO: implement part 1 logic
    return None


def solve_part2(raw: str):
    data = parse(raw)
    # TODO: implement part 2 logic
    return None
    
if __name__ == "__main__":
    from aoc.runner import run_day_from_file

    run_day_from_file(__file__, globals())
"""


TEST_TEMPLATE = """\
from aoc.year{year} import day{day:02d}


EXAMPLE_INPUT = \"\"\"\\
\"\"\"


def test_parse_example():
    data = day{day:02d}.parse(EXAMPLE_INPUT)
    # TODO: adjust expected structure
    assert isinstance(data, (list, tuple, str))


def test_part1_example():
    result = day{day:02d}.solve_part1(EXAMPLE_INPUT)
    # TODO: replace with the expected value from the problem example
    assert result is None


def test_part2_example():
    result = day{day:02d}.solve_part2(EXAMPLE_INPUT)
    # TODO: replace with the expected value from the problem example
    assert result is None
"""


def get_title(year: int, day: int) -> str:
    """Retrieve the puzzle title from adventofcode.com if available.

    Returns an empty string if the title cannot be fetched or parsed.
    """
    print("Retrieving title from adventofcode.com...")
    today = date.today()

    # - no title before 2015
    # - cannot know future years beyond this year
    # - before December, only titles up to (current year - 1) are guaranteed
    if year < 2015:
        print(f"[INFO] No title available for year {year} (before 2015).")
        return ""

    if today.month == 12:
        max_year = today.year
    else:
        max_year = today.year - 1

    if year > max_year:
        print(f"[INFO] No title available yet for year {year}.")
        return ""

    url = f"https://adventofcode.com/{year}/day/{day}"
    try:
        response = requests.get(url, timeout=10)
    except requests.RequestException as exc:
        print(f"[WARN] Failed to retrieve title: {exc}")
        return ""

    if response.status_code != 200:
        print(f"[WARN] Failed to retrieve title: HTTP {response.status_code}")
        return ""

    soup = BeautifulSoup(response.text, "html.parser")
    h2 = soup.find("h2")
    if not h2:
        print("[WARN] Could not find <h2> in the page.")
        return ""

    match = re.search(r"--- Day \d+: (.*) ---", h2.get_text())
    if not match:
        print("[WARN] Could not parse title from header.")
        return ""

    title = match.group(1).strip()
    print(f"[OK] Found title: {title}")
    return title


def ensure_year_package(year: int) -> Path:
    """Ensure the year package (aoc/yearYYYY) exists and has an __init__.py."""
    year_pkg = AOC_PACKAGE / f"year{year}"
    year_pkg.mkdir(parents=True, exist_ok=True)
    init_file = year_pkg / "__init__.py"
    if not init_file.exists():
        init_file.write_text("", encoding="utf-8")
    return year_pkg


def ensure_tests_year_dir(year: int) -> Path:
    """Ensure the tests/yearYYYY directory exists."""
    year_dir = TESTS_ROOT / f"year{year}"
    year_dir.mkdir(parents=True, exist_ok=True)
    return year_dir


def create_day_module(year: int, day: int) -> Path:
    """Create the dayDD.py module for the given year if it does not exist yet."""
    year_pkg = ensure_year_package(year)
    day_file = year_pkg / f"day{day:02d}.py"
    if day_file.exists():
        print(f"[INFO] {day_file} already exists, not touching it.")
        return day_file

    title = get_title(year, day)
    title_suffix = f": {title}" if title else ""
    content = DAY_TEMPLATE.format(year=year, day=day, title_suffix=title_suffix)
    day_file.write_text(dedent(content), encoding="utf-8")
    print(f"[OK] Created module: {day_file}")
    return day_file


def create_test_module(year: int, day: int) -> Path:
    """Create a basic pytest module for the given year and day."""
    year_tests_dir = ensure_tests_year_dir(year)
    test_file = year_tests_dir / f"test_day{day:02d}.py"
    if test_file.exists():
        print(f"[INFO] {test_file} already exists, not touching it.")
        return test_file

    content = TEST_TEMPLATE.format(year=year, day=day)
    test_file.write_text(dedent(content), encoding="utf-8")
    print(f"[OK] Created test: {test_file}")
    return test_file


def infer_december_day() -> Tuple[int | None, int | None]:
    """If today is between Dec 1st and Dec 25th (inclusive), return (year, day)."""
    today = date.today()
    if today.month == 12 and 1 <= today.day <= 25:
        return today.year, today.day
    return None, None


def ask_interactive() -> Tuple[int, int]:
    """Ask the user for year and day interactively."""
    while True:
        year_str = input("Year (e.g. 2025): ").strip()
        if year_str.isdigit():
            year = int(year_str)
            break
        print("Please enter a valid year (e.g. 2025).")

    while True:
        day_str = input("Day (1-25): ").strip()
        if day_str.isdigit():
            day = int(day_str)
            if 1 <= day <= 25:
                break
        print("Please enter a valid day between 1 and 25.")

    return year, day


def create_day(year: int, day: int) -> None:
    """Create both the day module and its corresponding test file."""
    create_day_module(year, day)
    create_test_module(year, day)


def main(argv=None):
    if argv is None:
        argv = sys.argv[1:]

    if len(argv) == 2:
        year = int(argv[0])
        day = int(argv[1])
    elif len(argv) == 0:
        year, day = infer_december_day()
        if year is not None and day is not None:
            print(
                f"[INFO] No arguments provided, using today's date: "
                f"year={year}, day={day:02d}"
            )
        else:
            print("[INFO] Not in December 1–25, asking for year and day interactively.")
            year, day = ask_interactive()
    else:
        print("Usage: create_day.py YEAR DAY")
        raise SystemExit(1)

    create_day(year, day)


if __name__ == "__main__":
    main()
