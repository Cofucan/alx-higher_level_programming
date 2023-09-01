#!/bin/bash
# This script sends a request to a server to make it respond with a specific message.
curl -sL -H "Origin: HolbertonSchool" -d "user_id=98" -X PUT 0.0.0.0:5000/catch_me
