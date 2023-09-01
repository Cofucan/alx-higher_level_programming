#!/usr/bin/python3
"""
Python script that takes in a URL and an email, it sends a POST request to
the passed URL with the email as a parameter, and displays the body of
the response (decoded in utf-8)
"""
import urllib.parse
import urllib.request
import sys


if __name__ == "__main__":
    URL = sys.argv[1]
    EMAIL = sys.argv[2]
    values = {'email': EMAIL}

    data = urllib.parse.urlencode(values).encode('ascii')
    req = urllib.request.Request(url=URL, data=data)
    with urllib.request.urlopen(req) as response:
        body = response.read()
        print(body.decode('utf-8'))
