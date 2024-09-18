#!/usr/bin/env python
from pathlib import Path
from typing import Optional, Union
import argparse
import os
import re


__version__ = "0.0.1"


class WC:
    def __init__(self, filePath: Union[str, Path, None] = None):
        if not filePath:
            self._parser = argparse.ArgumentParser(
                prog="wc",
                description="Python implementation of unix utility wc",
            )

            self._parser.add_argument(
                "file_name",
                metavar="path_to_file",
                type=str,
            )

            self._parser.add_argument(
                "-v",
                "--version",
                action="version",
                version=f"%(prog)s {__version__}",
            )

            self._parser.add_argument(
                "-l",
                "--lines",
                action="store_true",
                help="count lines in file",
            )

            self._parser.add_argument(
                "-c",
                "--bytes",
                action="store_true",
                help="count bytes in file",
            )

            self._parser.add_argument(
                "-m",
                "--chars",
                action="store_true",
                help="count chars in file",
            )

            self._parser.add_argument(
                "-w",
                "--words",
                action="store_true",
                help="count words in file",
            )

            self._parser.add_argument(
                "-L",
                "--max-line-lenght",
                action="store_true",
                help="length of max-length line",
            )

            self._args = self._parser.parse_args()
            self._filePath = Path(self._args.file_name).resolve()
        else:
            self._filePath = Path(filePath).resolve()

        if not self._filePath.exists():
            raise FileNotFoundError

    def count_lines(self) -> int:
        with open(self._filePath, encoding="utf-8") as f:
            return "Lines: " + str(sum(1 for _ in f)) + " " + str(self._filePath)

    def count_bytes(self) -> int:
        stats = os.stat(self._filePath)
        return "Bytes: " + str(stats.st_size) + " " + str(self._filePath)

    def count_chars(self) -> int:
        with open(self._filePath, encoding="utf-8") as f:
            return (
                "Chars: "
                + str(sum(len(line) for line in f))
                + " "
                + str(self._filePath)
            )
            # NOTE: bad!

    def count_words(self) -> int:
        with open(self._filePath, encoding="utf-8") as f:
            text = f.read()
            res = re.findall(r"\w+", text)
            return "Words: " + str(len(res)) + " " + str(self._filePath)

    def max_line_length(self) -> int:
        with open(self._filePath, encoding="utf-8") as f:
            return (
                "MLL: " + str(max(len(line) for line in f)) + " " + str(self._filePath)
            )

    def parser_output(self):
        """Use only with parser (filePath = None)"""
        funcs = [
            self.count_lines,
            self.count_bytes,
            self.count_chars,
            self.count_words,
            self.max_line_length,
        ]

        bools = [
            1 if self._args.lines else 0,
            1 if self._args.bytes else 0,
            1 if self._args.chars else 0,
            1 if self._args.words else 0,
            1 if self._args.max_line_lenght else 0,
        ]

        for i in range(len(funcs)):
            if bools[i]:
                print(funcs[i]())


if __name__ == "__main__":
    wc = WC()
    # print(wc._args)
    wc.parser_output()
