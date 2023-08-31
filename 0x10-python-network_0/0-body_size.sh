#!/bin/bash
# This script akes in a URL, sends a request to that URL, and displays the size of the body of the response
curl -s -w '%{size_download}\n' "$1" | tail -n 1
