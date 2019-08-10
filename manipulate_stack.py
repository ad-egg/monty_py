#!/usr/bin/python3
"""contains methods that manipulate stack"""

from sys import exit, stderr


def push(line_number, stack, line):
    """pushes a number onto a stack"""
    words = line.split()
    opcode = words[0]
    try:
        number = int(words[1])
    except IndexError or ValueError:
        print("L{:d}: usage: push <integer>".format(line_number), file=stderr)
        exit(1)
    stack.append(number)


def pop(line_number, stack):
    """pops top element of stack"""
    try:
        popped = stack.pop()
    except IndexError:
        print("L{:d}: can't pop an empty stack".format(line_number), file=stderr)
        exit(1)
    return popped


def swap(line_number, stack):
    """swaps top 2 elements of stack"""
    try:
        stack[-1], stack[-2] = stack[-2], stack[-1]
    except IndexError:
        print("L{:d}: can't swap, stack too short".format(line_number), file=stderr)
        exit(1)


def add(line_number, stack):
    """pops last element of stack and adds its value to new last element"""
    if len(stack) < 2:
        print("L{:d}: can't add, stack too short".format(line_number), file=stderr)
        exit(1)
    b = pop(line_number, stack)
    top = stack[-1]
    stack[-1] = top + b


def sub(line_number, stack):
    """pops last element of stack and subtracts its value to new last element"""
    if len(stack) < 2:
        print("L{:d}: can't sub, stack too short".format(line_number), file=stderr)
        exit(1)
    b = pop(line_number, stack)
    top = stack[-1]
    stack[-1] = top - b


def div(line_number, stack):
    """pops last element of stack and uses it to divide the new last element by it"""
    if len(stack) < 2:
        print("L{:d}: can't div, stack too short".format(line_number), file=stderr)
        exit(1)
    if stack[-1] == 0:
        print("L{:d}: division by zero".format(line_number), file=stderr)
        exit(1)
    b = pop(line_number, stack)
    top = stack[-1]
    stack[-1] = top / b


def mul(line_number, stack):
    """pops last element of stack and multiplies its value to new element"""
    if len(stack) < 2:
        print("L{:d}: can't mul, stack too short".format(line_number), file=stderr)
        exit(1)
    b = pop(line_number, stack)
    top = stack[-1]
    stack[-1] = top * b


def mod(line_number, stack):
    """pops last element of stack and uses it to modulus the new last element by it"""
    if len(stack) < 2:
        print("L{:d}: can't mod, stack too short".format(line_number), file=stderr)
        exit(1)
    if stack[-1] == 0:
        print("L{:d}: division by zero".format(line_number), file=stderr)
        exit(1)
    b = pop(line_number, stack)
    top = stack[-1]
    stack[-1] = top % b



