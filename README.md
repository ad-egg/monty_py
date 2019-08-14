# monty_py

### What is this?
This is an interpreter for Monty bytecodes files. [Monty](http://montyscoconut.github.io/) is a scripting language that is first compiled into Monty byte codes. It relies on a unique stack data structure with specific instructions to manipulate it. Monty byte codes usually have the `.m` extension.

### Why?
I basically redid [Monty bytecodes interpreter in C](https://github.com/ad-egg/monty) using Python programming language to review the concepts of file input/output, linked lists, and stack data structure in Python. For the project in C, I implemented a singly linked list for a stack. For this project, I started by using a list as a stack. However, when I reached the last of the advanced tasks for the project, I had to implement switching between a stack and queue so I switched to using a deque.

### Requirements
- Ubuntu 16.04 LTS
- Python 3.x.x

### How to use
`$ ./monty.py monty_byte_code_file_name.m`

A few Monty bytecode files are provided in the `byecodes` directory. For supported opcodes, look below.

### Example of usage
```
$ cat bytecodes/12.m
push 1
push 2
push 3
pall
add
pall
$ ./monty.py bytecodes/12.m
3
2
1
5
1
```

### Implemented opcodes
- **push**

  Usage: `push <int>` where `<int>` is an integer

  What it does: pushes an element to the stack.

- **pall**

  Usage: `pall`

  What it does: prints all the values on the stack, starting from the top of the stack.

- **pint**

  Usage: `pint`

  What it does: prints the value at the top of the stack followed by a new line.

- **pop**

  Usage: `pop`

  What it does: removes the top element of the stack.

- **swap**

  Usage: `swap`

  What it does: swaps the top two elements of the stack.

- **add**

  Usage: `add`

  What it does: adds the top two elements of the stack. The answer is stored in the second top element of the stack and the top element is removed so that the top element contains the result and the stack is one element shorter.

- **nop**

  Usage: `nop`

  What it does: nothing.

- **sub**

  Usage: `sub`

  What it does: subtracts the top element of the stack from the second element of the stack. The answer is stored in the second top element of the stack and the top element is removed so that the top element contains the result and the stack is one element shorter.

- **div**

  Usage: `div`

  What it does: divides the second top element of the stack by the first element of the stack. The answer is stored in the second top element of the stack and the top element is removed so that the top element contains the result and the stack is one element shorter.

- **mul**

  Usage: `mul`

  What it does: multiplies the top two elements of the stack. The answer is stored in the second top element of the stack and the top element is removed so that the top element contains the result and the stack is one element shorter.

- **mod**

  Usage: `mod`

  What it does: computes the remainder of the division of the second top element of the stack by the top element of the stack. The answer is stored in the second top element of the stack and the top element is removed so that the top element contains the result and the stack is one element shorter.

- **pchar**

  Usage: `pchar`

  What it does: prints the character at the top of the stack if it is a printable character.

- **pstr**

  Usage: `pstr`

  What it does: prints the string starting at the top of the stack.

- **rotl**

  Usage: `rotl`

  What it does: rotates the stack to the left.

- **rotr**

  Usage: `rotr`

  What it does: rotates the stack to the right.
