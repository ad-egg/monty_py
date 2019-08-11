#!/usr/bin/python3
"""this module contains the methods for print stack"""

from sys import exit, stderr


def pint(line_number, stack):
    """
    prints the top element of a stack
    """
    if len(stack) == 0:
        print("L{:d}: can't pint, stack empty".format(
                    line_number), file=stderr)
        exit(1)
    print(stack[-1])


def pall(line_number, stack):
    """
    prints all elements of a stack
    """
    length = len(stack)
    if length > 0:
        for i in range(length):
            # slices off last element of list and passes it to pint method
            pint(line_number, stack[:i + 1])


def pchar(line_number, stack):
    """
    prints the character of the integer value at top of stack
    """
    return

    
def pstr(line_number, stack):
    """
    prints the characters of the integer values in a stack
    """
    return
