#!/usr/bin/python3
"""Defines a class checking function"""


def inherits_from(obj, a_class):
    """Check if object is instance of class or inherited

    Args:
        obj (any): obj
        a_class (type): class to check
    Returns:
        True if obj is instance or inherited from class else false
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
