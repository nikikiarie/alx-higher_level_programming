#!/usr/bin/python3
"""Locked class definition"""


class LockedClass:
    """
    Prevents user from dynamically creating new instance attributes, except if the new instance attribute is called first_name
    """

    __slots__ = ["first_name"]
