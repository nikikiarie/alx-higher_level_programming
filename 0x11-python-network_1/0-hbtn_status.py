#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""


import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as r:
        cnt = r.read()
        print("Body response:")
        print("\t- type: {}".format(type(cnt)))
        print("\t- content: {}".format(cnt))
        print("\t- utf8 content: {}".format(cnt.decode('utf-8')))
