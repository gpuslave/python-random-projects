#!/usr/bin/env python
from pathlib import Path
import typing
import argparse


__version__ = "0.0.1"


def count_lines(filePath: Path) -> int:
    with open(filePath.resolve(), encoding="utf-8") as f:
        return sum(1 for line in f)


parser = argparse.ArgumentParser(
    prog="wc",
    description="Python implementation of unix utility wc",
)

parser.add_argument(
    "-v",
    "--version",
    action="version",
    version=f"%(prog)s {__version__}",
)

parser.add_argument(
    "file_name",
    metavar="path_to_file",
    type=str,
)

parser.add_argument(
    "-l",
    "--lines",
    action="store_true",
    help="count lines in file",
)

parser.add_argument(
    "-c",
    "--bytes",
    action="store_true",
    help="count bytes in file",
)

parser.add_argument(
    "-m",
    "--chars",
    action="store_true",
    help="count chars in file",
)

parser.add_argument(
    "-w",
    "--words",
    action="store_true",
    help="count words in file",
)

parser.add_argument(
    "-L",
    "--max-line-lenght",
    action="store_true",
    help="index of a max-length line",
)

args = parser.parse_args()
p = Path(args.file_name)
print(args)
print(count_lines(p))
