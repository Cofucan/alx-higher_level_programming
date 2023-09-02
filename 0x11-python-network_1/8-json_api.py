#!/usr/bin/python3
"""
Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import sys
import requests


if __name__ == "__main__":
    letter = '' if len(sys.argv) < 2 else sys.argv[1]
    URL = 'http://0.0.0.0:5000/search_user'
    data = {'q': letter}
    response = requests.post(URL, data=data)

    try:
        result = response.json()
        if result.get('id') is None:
            print("No result")
        else:
            print(f"[{result.get('id')}] {result.get('name')}")
    except ValueError:
        print("Not a valid JSON")
