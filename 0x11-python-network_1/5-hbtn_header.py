#!/usr/bin/python3
"""
sends a request to the URL and displays the value of the variable
X-Request-Id in the response header
"""
import sys
from requests import get


if __name__ == '__main__':
    rsp = get(sys.argv[1])

    print(rsp.headers.get('X-Request-Id'))
