#!/usr/bin/python3
"""
Python script that lists 10 commits (from the most recent to oldest) from
the repository of a GitHub user. It uses the GitHub API and prints all
commits in the format: `<sha>: <author name>`.
"""
import sys
import requests


if __name__ == "__main__":
    REPO_NAME = sys.argv[1]
    OWNER_NAME = sys.argv[2]
    URL = f"https://api.github.com/repos/{OWNER_NAME}/{REPO_NAME}/commits"

    response = requests.get(URL, timeout=5)
    commits = response.json()
    for idx, commit in enumerate(commits):
        if idx == 10:
            break
        sha = commit.get("sha")
        author = commit.get("commit").get("author").get("name")
        print(f"{sha}: {author}")
