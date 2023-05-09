#!/usr/bin/python3
def uppercase(str):
    upper = []
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            upper.append(chr(ord(c) - 32))
        else:
            upper.append(c)
    print("".join(upper))
