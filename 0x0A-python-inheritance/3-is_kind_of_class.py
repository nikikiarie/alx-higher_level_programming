#!/usr/bin/python
"""Defines a class checking function"""


def is_kind_of_class(obj, a_class):
    """Check if object is instance of class or inherited

    Args:
        obj (any): obj
        a_class (type): class to check
    Returns:
        True if obj is instance or inherited from class else false
    """
    if isinstance(obj, a_class):
        return True
    return False
