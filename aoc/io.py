from pathlib import Path
import os
from typing import Optional

import requests


AOC_INPUT_URL = "https://adventofcode.com/{year}/day/{day}/input"


def get_resources_root() -> Path:
    env = os.getenv("AOC_INPUT_DIR")
    if env:
        return Path(env)
    return Path(__file__).resolve().parents[1] / "resources"


def input_path(year: int, day: int) -> Path:
    """
    Build the input file path for a given year and day.

    IMPORTANT: day is *not* zero-padded, to match Java project structure.
    Example: resources/aoc2024/day1.txt
    """
    root = get_resources_root()
    return root / f"aoc{year}" / f"day{day}.txt"


def get_session_token() -> Optional[str]:
    """
    Try to retrieve the AoC session token.

    Priority:
    1. Try to read it from the browser using browser_cookie3.
    2. Fallback to environment variable AOC_SESSION.
    """
    # 1) Try browser cookies
    try:
        import browser_cookie3

        # Tries multiple browser loaders
        for loader in (
                browser_cookie3.brave,
                browser_cookie3.chrome,
                browser_cookie3.firefox,
                browser_cookie3.edge,
                browser_cookie3.chromium,
        ):
            try:
                if loader is None:
                    continue

                cj = loader(domain_name="adventofcode.com")
                for cookie in cj:
                    if cookie.name == "session":
                        # Return the token immediately upon success
                        return cookie.value
            except Exception as e:
                pass
    except ImportError:
        pass

    # 2) Fallback to environment variable
    env_token = os.getenv("AOC_SESSION")
    if env_token:
        return env_token

    return None


def download_input(year: int, day: int, dest: Path) -> bool:
    session_token = get_session_token()
    if not session_token:
        print("[WARN] AOC_SESSION not set, cannot download input.")
        return False

    url = AOC_INPUT_URL.format(year=year, day=day)
    headers = {"User-Agent": "github.com/dapitch666/AdventOfCode (Python AoC helper)"}
    cookies = {"session": session_token}

    try:
        response = requests.get(url, headers=headers, cookies=cookies, timeout=10)
    except requests.RequestException as exc:
        print(f"[ERROR] Failed to download input: {exc}")
        return False

    if response.status_code != 200:
        print(f"[ERROR] Failed to download input: HTTP {response.status_code}")
        return False

    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(response.text.rstrip("\n"), encoding="utf-8")
    print(f"[OK] Downloaded input to {dest}")
    return True


def load_input(year: int, day: int) -> str:
    path = input_path(year, day)
    if not path.exists():
        print(f"[INFO] Input file {path} does not exist, trying to download...")
        if not download_input(year, day, path):
            print("[WARN] Could not obtain input.")
            return ""
    return path.read_text(encoding="utf-8").rstrip("\n")