#!/usr/bin/python3
def safe_print_integer(value):
    try:
        val = int(value)
        print("{:d}".format(val))
    except Exception:
        return False

    return True
