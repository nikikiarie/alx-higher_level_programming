#!/usr/bin/python3
"""Defines json-to-string function"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
