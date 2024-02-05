#!/usr/bin/python3
"""Defines inherited list"""


class MyList(list):
    """Uses sorted printing gor list"""

    def printed_sorted(self):
        """Print a list in asc order"""
        print(sorted(self));
