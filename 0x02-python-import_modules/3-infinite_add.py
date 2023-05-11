#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    total = 0
    args = sys.argv

    if len(args) > 1:
        for arg in sys.argv[1:]:
            total += int(arg)

    print(total)
