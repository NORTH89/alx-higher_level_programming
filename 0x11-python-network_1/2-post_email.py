#!/usr/bin/python3
"""Sends a req to URL and display the res body.
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf8"))
