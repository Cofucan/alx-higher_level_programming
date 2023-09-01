#!/bin/bash
# This script takes in a URL and displays all HTTP methods the server will accept.
curl -Is "$1" | grep -Po '(?<=Allow: )\w+'
