#!/usr/bin/python3
"""Defines a class checking function"""


def is_same_class(obj, a_class):
    """Check if object is instance of class

    Args:
        obj (any): obj
        a_class (type): class to check
    Returns:
        True if obj is instance of class else false
    """
    if type(obj) == a_class:
        return True
    return False
