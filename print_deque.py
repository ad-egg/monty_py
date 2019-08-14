#!/usr/bin/python3
"""this module contains the methods for print stack"""

from sys import exit, stderr


def pint(line_number, structure, s_q):
    """
    prints the top element of a stack
    """
    if len(structure) == 0:
        print("L{:d}: can't pint, {} empty".format(
                    line_number, s_q), file=stderr)
        exit(1)
    print(structure[0])


def pall(line_number, structure):
    """
    prints all elements of a stack starting from the top
    """
    length = len(structure)
    if length > 0:
        for i in range(length):
            print(structure[i])


def pchar(line_number, structure, s_q):
    """
    prints the character of the integer value at top of stack
    """
    if len(structure) == 0:
        print("L{:d}: can't pchar, {} empty".format(
                    line_number, s_q), file=stderr)
        exit
    number = structure[0]
    if number > 32 and number < 127:
        print(chr(number))
    else:
        print("L{:d}: can't pchar, value out of range".format(), file=stderr)
        exit(1)

    
def pstr(line_number, structure):
    """
    prints the characters of the integer values in a stack
    """
    length = len(structure)
    if length > 0:
        for i in range(length):
            number = structure[i]
            if number > 32 and number < 127:
                print("{}".format(chr(number)), end="")
            else:
                break
    print("")
