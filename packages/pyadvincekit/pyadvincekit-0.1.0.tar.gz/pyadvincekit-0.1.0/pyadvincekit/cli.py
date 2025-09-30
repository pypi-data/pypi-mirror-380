"""
Command line interface for PyAdvanceKit.
"""

from __future__ import annotations

import argparse
import sys

from . import __version__


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="pyadvincekit",
        description="PyAdvanceKit command line interface",
    )
    parser.add_argument(
        "--version",
        action="store_true",
        help="Show the PyAdvanceKit version and exit",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.version:
        print(__version__)
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())


