#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    res = 0
    for i in reversed(roman_string):
        num = data[i]
        res += num if res < num * 5 else -num
    return res

