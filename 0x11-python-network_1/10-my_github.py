#!/usr/bin/python3
"""
takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""
from sys import argv
from requests import get


if __name__ == '__main__':
    rsp = get("https://api.github.com/user", auth=(argv[1], argv[2]))
    obj = rsp.json()
    print(obj.get('id'))
