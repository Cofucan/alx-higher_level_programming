#!/usr/bin/python3
"""
Python script that in a URL, sends a request to the URL and displays the
body of the response (decoded in utf-8). It also handles any
`urllib.error.HTTPError` errors.
"""
import urllib.error
import urllib.request
import sys


if __name__ == "__main__":
    URL = sys.argv[1]

    req = urllib.request.Request(url=URL)
    try:
        with urllib.request.urlopen(req) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as err:
        print(f"Error code: {err.code}")
