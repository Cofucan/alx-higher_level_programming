#!/usr/bin/python3
"""
Python script that takes some GitHub credentials (username and password)
and uses the GitHub API to display the id
"""
import sys
import requests


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, password))
    print(response.json().get("id"))
