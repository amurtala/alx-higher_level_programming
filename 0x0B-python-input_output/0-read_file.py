#!/bin/usr/python3
"""Module 0-read_file.
Read and print file
"""

def read_file(filename=""):
    """A function that reads a text 
    file (UTF8) and prints it to stdout.
    Args:
        - filename: name of file
    """

    with open(filename) as f:
        print(f.read(), end="")
