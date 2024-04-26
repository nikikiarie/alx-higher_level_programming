#!/usr/bin/python3
"""
Script that use Github api tp list 10 most recent commits of a repo
"""
from requests import get
from sys import argv


if __name == 'main':
    add = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])

    rsp = get(url)
    obj = rsp.json()
    try:
        for a in range(10):
            print("{}: {}".format(obj[a].get("sha"), obj[a].get("commit").get("author").get("name")))
    except IndexError:
        pass
