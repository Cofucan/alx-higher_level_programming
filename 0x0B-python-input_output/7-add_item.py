#!/usr/bin/python3
"""Load, add, save"""
import os
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = list(sys.argv[1:])
filename = "add_item.json"

if os.path.isfile(filename):
    from_file = list(load_from_json_file(filename))
    args.extend(from_file)

save_to_json_file(args, filename)
