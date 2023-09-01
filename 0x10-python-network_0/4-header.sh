#!/bin/bash
# This script takes in a URL and sends a GET request to the URL, and displays the body of the response
# It also sends custom headers along with the request.
curl -s -H "X-School-User-Id: 98" -X GET "$1"
