#!/usr/bin/python3
"""contains main and line reading functions of bytecodes interpreter"""

import os

from manipulate_stack import *
from print_stack import *

from sys import argv, exit, stderr


def line_reader(line_number, line, stack):
    """
    takes a string, splits it, executes any commands on a stack
    """
    skip = {
        "nop", "#",
    }
    printing = {
        "pall": "pall(line_number, stack)",
        "pint": "pint(line_number, stack)",
        "pstr": "pstr(line_number, stack)",
        "pchar": "pchar(line_number, stack)",
    }
    manipulating = {
        "add": "add(line_number, stack)",
        "sub": "sub(line_number, stack)",
        "mul": "mul(line_number, stack)",
        "div": "div(line_number, stack)",
        "mod": "mod(line_number, stack)",
        "push": "push(line_number, stack, line)",
        "pop": "pop(line_number, stack)",
        "rotl": "rotl(line_number, stack)",
        "rotr": "rotr(line_number, stack)",
        "swap": "swap(line_number, stack)",
    }
    words = line.split()
    try:
        opcode = words[0]
        if opcode in skip:
            return
        elif opcode in printing.keys():
            eval(printing[opcode])
        elif opcode in manipulating.keys():
            eval(manipulating[opcode])
        else:
            print("L{:d}: unknown instruction '{}'".format(
                        line_number, words[0]), file=stderr)
            exit(1)
    except IndexError:
        return


def monty(argv):
    """
    opens a Monty bytecodes file, reads it, and
    executes the commands on a stack data structure

    """
    num_args = len(argv)
    if num_args != 2:
        # user must enter only one argument
        print("Usage: ./monty.py <file_name>", file=stderr)
        exit(1)
    if os.path.isfile(argv[1]) is False:
        # cannot find the file
        print("Error: Can't open file '{}'".format(argv[1]), file=stderr)
        exit(1)
    if os.access(argv[1], os.R_OK) is False:
        # user does not have permission to read the file
        print("Error: Can't open file '{}'".format(argv[1]), file=stderr)
        exit(1)
    with open(argv[1]) as f:
        lines = f.read()
    lines = lines.split("\n")
    line_number = 0
    stack = []
    for line in lines:
        # send entire line to helper function
        # helper function splits line and manipulates stack
        line_reader(line_number, line, stack)
        line_number += 1
    return


if __name__ == "__main__":
    monty(argv)
