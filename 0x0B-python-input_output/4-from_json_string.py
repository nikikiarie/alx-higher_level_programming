#!/usr/bin/python3
"""Defines json-to-string function"""
import json


def from_json_string(my_str):
    """Return JSON string"""
    return json.loads(my_str)
