#!/usr/bin/python3
for u in range(10):
    for v in range(10):
        if int(u) >= int(v):
            continue
        elif int(u) == 8 and int(v) == 9:
            print("{}{}".format(u, v))
            continue
        print("{}{}, ".format(u, v), end="")
