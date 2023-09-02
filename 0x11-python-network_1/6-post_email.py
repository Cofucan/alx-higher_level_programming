#!/usr/bin/python3
"""
Python script that takes in a URL and an email, it sends a POST request to
the passed URL with the email as a parameter, and displays the body of
the response.
"""
import sys
import requests


if __name__ == "__main__":
    URL = sys.argv[1]
    EMAIL = sys.argv[2]
    data = {'email': EMAIL}

    resp = requests.post(URL, data=data, timeout=5).text
    print(resp)
