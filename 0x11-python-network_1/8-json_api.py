#!/usr/bin/python3
""" Sends a POST request to the passed URL with the email as a parameter"""

import sys
import requests


if __name__ == "__main__":
    query = "" if len(sys.argv) == 1 else sys.argv[1]
    payload = {"q": query}

    req = requests.post("http://0.0.0.0:5000/search_user", data=payload)
    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
