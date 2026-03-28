#!/usr/bin/env python3
"""Print local timestamp for plan filename: YYYY-MM-DD-HHmm."""

from datetime import datetime


def main() -> None:
    print(datetime.now().strftime("%Y-%m-%d-%H%M"))


if __name__ == "__main__":
    main()
