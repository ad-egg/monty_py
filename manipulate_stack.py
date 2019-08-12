#!/usr/bin/python3
"""contains methods that manipulate stack"""

from sys import exit, stderr


def push(line_number, structure, line, s_q):
    """pushes a number onto a stack"""
    words = line.split()
    opcode = words[0]
    try:
        number = int(words[1])
    except IndexError or ValueError:
        print("L{:d}: usage: push <integer>".format(line_number), file=stderr)
        exit(1)
    if sq == "stack":
        structure.appendleft(number)
    else:
        structure.append(number)


def pop(line_number, structure):
    """pops top element of stack"""
    try:
        popped = structure.popleft()
    except IndexError:
        print("L{:d}: can't pop an empty stack".format(line_number), file=stderr)
        exit(1)
    return popped


def swap(line_number, structure):
    """swaps top 2 elements of stack"""
    try:
        stack[0], stack[1] = stack[1], stack[0]
    except IndexError:
        print("L{:d}: can't swap, stack too short".format(line_number), file=stderr)
        exit(1)


def add(line_number, structure):
    """pops last element of stack and adds its value to new last element"""
    if len(structure) < 2:
        print("L{:d}: can't add, stack too short".format(line_number), file=stderr)
        exit(1)
    b = pop(line_number, structure)
    top = structure[0]
    structure[0] = top + b


def sub(line_number, structure):
    """pops last element of stack and subtracts its value to new last element"""
    if len(structure) < 2:
        print("L{:d}: can't sub, stack too short".format(line_number), file=stderr)
        exit(1)
    b = pop(line_number, structure)
    top = structure[0]
    structure[0] = top - b


def div(line_number, structure):
    """pops last element of stack and uses it to divide the new last element by it"""
    if len(structure) < 2:
        print("L{:d}: can't div, stack too short".format(line_number), file=stderr)
        exit(1)
    if structure[0] == 0:
        print("L{:d}: division by zero".format(line_number), file=stderr)
        exit(1)
    b = pop(line_number, structure)
    top = structure[0]
    structure[0] = top / b


def mul(line_number, structure):
    """pops last element of stack and multiplies its value to new element"""
    if len(structure) < 2:
        print("L{:d}: can't mul, stack too short".format(line_number), file=stderr)
        exit(1)
    b = pop(line_number, structure)
    top = structure[0]
    structure[0] = top * b


def mod(line_number, structure):
    """pops last element of stack and uses it to modulus the new last element by it"""
    if len(structure) < 2:
        print("L{:d}: can't mod, stack too short".format(line_number), file=stderr)
        exit(1)
    if structure[0] == 0:
        print("L{:d}: division by zero".format(line_number), file=stderr)
        exit(1)
    b = pop(line_number, structure)
    top = structure[0]
    structure[0] = top % b


def rotl(line_number, structure):
    """rotates stack to the left so that top of stack becomes bottom of stack"""
    length = len(structure)
    if length > 2:
        top = pop(line_number, structure)
        structure.insert(0, top)
    elif length == 2:
        swap(line_number, structure)


def rotr(line_number, structure):
    """rotates stack to the right so that bottom of stack becomes top of stack"""
    length = len(structure)
    if length > 2:
        bottom = structure.pop(0)
        structure.append(bottom)
    elif length == 2:
        swap(line_number, structure)
