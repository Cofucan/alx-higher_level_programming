#!/bin/bash
# This script takes in a URL and sends a JSON POST request with the contents of a file also passed as argument to the passed URL, and displays the body of the response
curl -s -d "@$2" -H "Content-Type: application/json" -X POST "$1"
