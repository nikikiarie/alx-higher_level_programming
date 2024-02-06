#!/usr/bin/python3
"""Task 7"""



import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

items = list(sys.argv[1:])

try:
    dta = load_from_json_file("add_item.json")
except FileNotFoundError:
    dta = []

dta.extend(items)
save_to_json_file(dta, 'add_item.json')
