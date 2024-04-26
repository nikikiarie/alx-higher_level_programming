#!/usr/bin/python3
"""
Python script that fetches an URL with requests package
"""
from requests import get


if __name__ == "__main__":
    res = get('https://alx-intranet.hbtn.io/status')
    txt = res.text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(
        type(txt), txt))
