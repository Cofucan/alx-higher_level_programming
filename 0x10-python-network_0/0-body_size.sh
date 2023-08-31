#!/bin/bash
# This script akes in a URL, sends a request to that URL, and displays the size of the body of the response

url="$1"

curl -s -w '%{size_download}\n' "$url" | tail -n 1
