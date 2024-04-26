#!/usr/bin/python3
"""
Displays the value of the X-Request-Id variable
found in the header of the response
"""


if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as res:
        print(res.headers["X-Request-Id"])
