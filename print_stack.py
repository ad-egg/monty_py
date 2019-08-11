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
    prints all elements of a stack starting from the top
    """
    length = len(stack)
    if length > 0:
        for i in range(length):
            # slices off last element of list and passes it to pint method
            pint(line_number, stack[:length - i])


def pchar(line_number, stack):
    """
    prints the character of the integer value at top of stack
    """
    if len(stack) == 0:
        print("L{:d}: can't pchar, stack empty".format(
                    line_number), file=stderr)
        exit
    number = stack[-1]
    if number > 32 and number < 127:
        print(chr(number))
    else:
        print("L{:d}: can't pchar, value out of range".format(), file=stderr)
        exit(1)

    
def pstr(line_number, stack):
    """
    prints the characters of the integer values in a stack
    """
    length = len(stack)
    if length > 0:
        stack2 = stack[:]
        for i in range(length):
            number = stack2[-1]
            if number > 32 and number < 127:
                print("{}".format(chr(number)), end="")
                stack2.pop()
            else:
                break
    print("")
