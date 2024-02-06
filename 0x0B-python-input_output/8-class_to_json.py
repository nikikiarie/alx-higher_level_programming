#!/usr/bin/python3
"""Defines clas to json function"""

def class_to_json(obj):
    """Return dictionary representaion"""
    return obj.__dict__
