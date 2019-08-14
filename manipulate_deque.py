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
    if s_q == "stack":
        structure.appendleft(number)
    else:
        structure.append(number)


def pop(line_number, structure, s_q):
    """pops top element of stack"""
    try:
        popped = structure.popleft()
    except IndexError:
        print("L{:d}: can't pop an empty {}".format(line_number, s_q), file=stderr)
        exit(1)
    return popped


def swap(line_number, structure, s_q):
    """swaps top 2 elements of stack"""
    try:
        structure[0], structure[1] = structure[1], structure[0]
    except IndexError:
        print("L{:d}: can't swap, {} too short".format(line_number, s_q), file=stderr)
        exit(1)


def add(line_number, structure, s_q):
    """pops last element of stack and adds its value to new last element"""
    if len(structure) < 2:
        print("L{:d}: can't add, {} too short".format(line_number, s_q), file=stderr)
        exit(1)
    b = pop(line_number, structure, s_q)
    top = structure[0]
    structure[0] = top + b


def sub(line_number, structure, s_q):
    """pops last element of stack and subtracts its value to new last element"""
    if len(structure) < 2:
        print("L{:d}: can't sub, {} too short".format(line_number, s_q), file=stderr)
        exit(1)
    b = pop(line_number, structure, s_q)
    top = structure[0]
    structure[0] = top - b


def div(line_number, structure, s_q):
    """pops last element of stack and uses it to divide the new last element by it"""
    if len(structure) < 2:
        print("L{:d}: can't div, {} too short".format(line_number, s_q), file=stderr)
        exit(1)
    if structure[0] == 0:
        print("L{:d}: division by zero".format(line_number), file=stderr)
        exit(1)
    b = pop(line_number, structure, s_q)
    top = structure[0]
    structure[0] = top / b


def mul(line_number, structure, s_q):
    """pops last element of stack and multiplies its value to new element"""
    if len(structure) < 2:
        print("L{:d}: can't mul, {} too short".format(line_number, s_q), file=stderr)
        exit(1)
    b = pop(line_number, structure, s_q)
    top = structure[0]
    structure[0] = top * b


def mod(line_number, structure, s_q):
    """pops last element of stack and uses it to modulus the new last element by it"""
    if len(structure) < 2:
        print("L{:d}: can't mod, {} too short".format(line_number, s_q), file=stderr)
        exit(1)
    if structure[0] == 0:
        print("L{:d}: division by zero".format(line_number), file=stderr)
        exit(1)
    b = pop(line_number, structure, s_q)
    top = structure[0]
    structure[0] = top % b


def rotl(line_number, structure, s_q):
    """rotates stack to the left so that top of stack becomes bottom of stack"""
    length = len(structure)
    if length > 2:
        structure.rotate(-1)
    elif length == 2:
        swap(line_number, structure, s_q)


def rotr(line_number, structure, s_q):
    """rotates stack to the right so that bottom of stack becomes top of stack"""
    length = len(structure)
    if length > 2:
        structure.rotate(1)
    elif length == 2:
        swap(line_number, structure, s_q)
