#!/usr/bin/python3
"""main function of bytecode file command interpreter"""

import os

from sys import argv, exit, stderr


def pall(stack):
    """
    prints all elements of a stack
    """
    for element in stack:
        print(element)


def pint(line_number, stack):
    """
    prints the top element of a stack
    """
    length = len(stack)
    if length == 0:
        print("L{:d}: can't pint, stack empty".format(line_number), file=stderr)
        exit(1)
    print(stack[length - 1])


def line_reader(line_number, line, stack):
    """
    takes a string, splits it, executes any commands on a stack
    """
    skip = {
        "nop", "#",
    }
    printing = {
        "pall", "pint", "pstr", "pchar",
    }
    math = {
        "add", "sub", "mul", "div", "mod",
    }
    manipulating = {
        "push", "pop", "rotl", "rotr", "swap",
    }
    words = line.split(" ")
    opcode = words[0]
    if opcode in skip:
        return
    elif opcode in printing:
        if opcode == "pall":
            pall(stack)
        elif opcode == "pint":
            pint(line_number, stack)
    elif opcode in manipulating:
        # check words[1] exists and that it is an integer
        return
    elif opcode in maths:
        # check that there are at least 2 elements in stack
        return
    print("L{:d}: unknown instruction '{}'".format(line_number, words[0]), file=stderr)
    exit(1)


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
