#!/usr/bin/python3
"""
sends a request to the URL and displays the body of the response
"""
from sys import argv
from requests import get


if __name__ == '__main__':
    rsp = get(argv[1])
    if rsp.status_code >= 400:
        print("Error code: {}".format(rsp.status_code))
    else:
        print(rsp.text)
