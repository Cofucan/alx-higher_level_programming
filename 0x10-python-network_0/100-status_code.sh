#!/bin/bash
# This script takes in a URL and displays only the status code of the response
awk 'NR==1{printf "%s", $2}' headers "$(curl -sI "$1" -o headers)"
