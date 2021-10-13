#!/usr/bin/python3
# 1-number_of_lines.py
"""Defines a text file line-counting function."""


def number_of_lines(filename=""):
    """Return the number of lines in a text file."""
    lines = 0
    with open(filename) as reader:
        for line in reader:
            lines += 1
    return lines
