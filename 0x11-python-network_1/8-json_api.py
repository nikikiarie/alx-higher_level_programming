#!/usr/bin/python3
"""
Sends a request to the URL and displays the body of the response
"""
from requests import post
from sys import argv


if __name__ == '__main__':
    ltr = "" if len(argv) == 1 else argv[1]
    dta = {"q": ltr}
    url = "http://0.0.0.0:5000/search_user"

    rsp = post(url, data=dta)
    try:
        dt = rsp.json()
        if dt == {}:
            print("No result")
        else:
            print("[{}] {}".format(dt.get("id"), dt.get("name")))
    except ValueError:
        print("Not a valid JSON")
