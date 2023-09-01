#!/bin/bash
# This script takes in a URL and sends a POST request to the passed URL, and displays the body of the response
curl -s -H "email: test@gmail.com" -H "subject: I will always be here for PLD" -X POST "$1"
