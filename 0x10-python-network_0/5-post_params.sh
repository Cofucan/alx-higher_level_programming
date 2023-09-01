#!/bin/bash
# This script takes in a URL and sends a POST request to the passed URL, and displays the body of the response
# It also sends custom headers along with the request.
curl -s -d "email=test@gmail.com" -d "subject=I will always be here for PLD" -X POST "$1"
