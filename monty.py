#!/usr/bin/python3
"""contains main and line reading functions of bytecodes interpreter"""

import os

from manipulate_stack import *
from print_stack import *

from collections import deque
from sys import argv, exit, stderr


def line_reader(line_number, line, stack, s_q):
    """
    takes a string, splits it, executes any commands on a stack or queue
    """
    skip = {
        "nop", "#",
    }
    t = {
        "stack", "queue",
    }
    printing = {
        "pall": "pall(line_number, structure)",
        "pint": "pint(line_number, structure, s_q)",
        "pstr": "pstr(line_number, structure)",
        "pchar": "pchar(line_number, structure, s_q)",
    }
    manipulating = {
        "add": "add(line_number, structure, s_q)",
        "sub": "sub(line_number, structure, s_q)",
        "mul": "mul(line_number, structure, s_q)",
        "div": "div(line_number, structure, s_q)",
        "mod": "mod(line_number, structure, s_q)",
        "push": "push(line_number, structure, line, s_q)",
        "pop": "pop(line_number, structure, s_q)",
        "rotl": "rotl(line_number, structure)",
        "rotr": "rotr(line_number, structure)",
        "swap": "swap(line_number, structure, s_q)",
    }
    words = line.split()
    try:
        opcode = words[0]
        if opcode in t:
            s_q = opcode
        elif opcode in skip:
            return s_q
        elif opcode in printing.keys():
            eval(printing[opcode])
        elif opcode in manipulating.keys():
            eval(manipulating[opcode])
        else:
            print("L{:d}: unknown instruction '{}'".format(
                        line_number, words[0]), file=stderr)
            exit(1)
    except IndexError:
        return s_q
    return s_q


def monty(argv):
    """
    opens a Monty bytecodes file, reads it, and
    executes the commands on a stack/queue data structure

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
    s_q = "stack"
    structure = deque([])
    for line in lines:
        # send entire line to helper function
        # helper function splits line and manipulates stack/queue
        s_q = line_reader(line_number, line, structure, s_q)
        line_number += 1
    return


if __name__ == "__main__":
    monty(argv)
