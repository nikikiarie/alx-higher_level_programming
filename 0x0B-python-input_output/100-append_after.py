#!/usr/bin/python3
""" append-after function"""


def append_after(filename="", search_string="", new_string=""):
    """appends string after search line"""
    with open(filename, 'r', encoding='utf-8') as f:
        lines = []
        while True:
            line = f.readline()
            if line == "":
                break
            lines.append(line)
            if search_string in line:
                line.append(new_string)
    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(lines)
