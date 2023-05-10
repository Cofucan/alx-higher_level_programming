#!/usr/bin/python3
for idx, char in enumerate("abcdefghijklmnopqrstuvwxyz"[::-1], 1):
    if idx & 1 != 0:
        print("{}".format(char), end="")
    elif idx & 1 == 0:
        print("{}".format(chr(ord(char) - 32)), end="")
