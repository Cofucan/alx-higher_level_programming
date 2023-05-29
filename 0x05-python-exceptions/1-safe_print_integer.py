#!/usr/bin/python3
def safe_print_integer(value):
    try:
        val = int(value)
        print("{:d}".format(val))
        return True
    except Exception:
        return False

