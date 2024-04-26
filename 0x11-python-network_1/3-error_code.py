#!/usr/bin/python3
"""
Sends a request to the URL and displays the body of the response
(decoded in utf-8)
"""
from urllib import error, request
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as res:
            cnt = res.read()
            print(cnt.decode('utf-8'))
    except error.HTTPError as er:
        print('Error code: {}'.format(er.code))
