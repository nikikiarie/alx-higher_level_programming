#!/usr/bin/python3
"""reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Print content of text file"""

    with open(filename, encoding="utf-8") as f:
        print(f.read(),end="")
