#!/usr/bin/python3
"""This module contains a function that splits text by specified delimiters."""


def text_indentation(text):
    """Prints text separated by deliiters, line by line.

    Args:
        text (str): Text to print.

    Raises:
        TypeError: If text given is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_text = text.replace('?', '.').replace(':', '.')
    splited = new_text.split('.')
    for line in splited[:-1]:
        print(line.strip())
        print("")
    print(splited[-1].strip())
