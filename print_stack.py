#!/usr/bin/python3
"""this module contains the methods for print stack"""

from sys import exit, stderr


def pall(stack):
    """
    prints all elements of a stack
    """
    length = len(stack)
    for i in range(length - 1, -1, -1):
        print(stack[i])


def pint(line_number, stack):
    """
    prints the top element of a stack
    """
    length = len(stack)
    if length == 0:
        print("L{:d}: can't pint, stack empty".format(
                    line_number), file=stderr)
        exit(1)
    print(stack[length - 1])
