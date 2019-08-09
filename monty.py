#!/usr/bin/python3
"""main function of bytecode file command interpreter"""

import os

from sys import argv


def monty(argv):
    """

    """
    num_args = len(argv)
    if num_args != 2:
        # user must enter only one argument
        print("Usage: ./monty.py <file_name>")
        return
    if os.path.isfile(argv[1]) is False:
        # cannot find the file
        print("'{}' is not a valid file path".format(argv[1]))
        return
    if os.access(argv[1], os.R_OK) is False:
        # user does not have permission to read the file
        print("you do not have permission to read '{}'".format(argv[1]))
        return
    with open(argv[1]) as f:
        lines = f.read()
    for line in lines:
        # send entire line to helper function
        # helper function splits line and manipulates stack
        continue
    return

if __name__=="__main__":
    monty(argv)
