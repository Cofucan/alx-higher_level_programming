#!/usr/bin/python3
for s in "abcdefghijklmnopqrstuvwxyz":
    if s == "q" or s == "e":
        continue
    print("{}".format(s), end="")
