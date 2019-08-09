#!/usr/bin/python3
"""main function of bytecode file command interpreter"""

import os

from sys import argv


def line_reader(line):
    """
    takes a string, splits it, executes any commands on a stack
    """
    skip = {
        "nop",
        "#",
    }
    printing = {
        "pall",
        "pint",
        "pstr",
        "pchar",
    }
    manipulating = {
        "add",
        "sub",
        "mul",
        "div",
        "mod",
        "push",
        "pop",
        "rotl",
        "rotr",
        "swap",
    }
    words = line.split(" ")
    if words[0] in skip:
        return
    elif words[0] in printing:
        return
    elif words[0] in manipulating:
        return


def monty(argv):
    """
    opens a Monty bytecodes file, reads it, and
    executes the commands on a stack data structure

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
        line_reader(line)
        continue
    return

if __name__=="__main__":
    monty(argv)
