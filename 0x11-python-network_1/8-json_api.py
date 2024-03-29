#!/usr/bin/python3
""" Sends a POST request to the passed URL with the email as a parameter"""
import requests
import sys

url = "http://0.0.0.0:5000/search_user"

if len(sys.argv) > 1:
    q = sys.argv[1]
else:
    q = ""

r = requests.post(url, data={"q": q})

try:
    res = r.json()
except ValueError:
    print("Not a valid JSON")

if not res:
    print("No result")
else:
    for user in res:
        print("[{}] {}".format(user["id"], user["name"]))
