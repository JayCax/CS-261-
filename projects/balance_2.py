# Name: John-Francis Caccamo
# Date: 4 / 21 / 20
# balance_2.py
# Description:
# ===================================================
# Using a stack to check for unbalanced parentheses
# ===================================================

import sys


# Checks whether the input string is balanced
# param: input string
# returns True if string is balanced, otherwise returns False

class Stack:
    def __init__(self):
        self._stack = []
        self._stack_size = 0

    def get_stack(self):
        return self._stack

    def push(self, val_param):
        self._stack += [val_param]
        self._stack_size += 1
        # self._stack.append(val_param)

    def pop(self):
        pop_val = self._stack[self._stack_size - 1]
        self._stack = self._stack[:self._stack_size - 1]
        self._stack_size -= 1
        return pop_val

    def top(self):
        return self._stack[self._stack_size - 1]

    def is_empty(self):
        if not self._stack:
            return True
        else:
            return False

    """def stack_recursive(self):
        if self.is_empty():  # if base case of empty string is reached
            return True  # return True

        else:  # recursive case will check corresponding indices at start and end of string parameter
            if self._stack[0] == self._stack[-1]:  # compare first and last character to establish equality
                return self.stack_recursive(self._stack[1:-1])  # recursively check 2nd letter to 2nd to last letter and so on

        return False  # return False at the first set of un-matching string"""


def stack_recursive(stack_list):

    if len(stack_list) <= 1:  # if base case of empty string is reached
        return True  # return True

    else:  # recursive case will check corresponding indices at start and end of string parameter
        if stack_list[0] == stack_list[-1]:  # compare first and last character to establish equality
            return stack_recursive(stack_list[1:-1])  # recursively check 2nd letter to 2nd to last letter and so on

    return False  # return False at the first set of un-matching string


def is_balanced(input_string):
    # initialize an empty list as the stack
    stack = Stack()
    # if input_string = "":
    # iterate over each character in the string

    for i in input_string:
        # FIXME: You will write this function
        stack.push(i)

    if stack_recursive(stack.get_stack()):
        return True
    else:
        return False

if __name__ == '__main__':
    # get input string
    _input_string = sys.argv[1]  # DO NOT MODIFY
    balanced = is_balanced(_input_string)

    if balanced:
        print("The string {} is balanced".format(_input_string))
    else:
        print("The string {} is not balanced".format(_input_string))


"""if __name__ == '__main__':
    # get input string
    # _input_string = sys.argv[1]  # DO NOT MODIFY
    _input_string = "tacocat"
    balanced = is_balanced(_input_string)

    if balanced:
        print("The string {} is balanced".format(_input_string))
    else:
        print("The string {} is not balanced".format(_input_string))"""
