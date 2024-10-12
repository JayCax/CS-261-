# Name: John-Francis Caccamo
# Date: 4 / 21 / 20
# balance_2.py
# Description:
# ===================================================
# This is the balance.py file which will use a stack to
# check for unbalanced parentheses, brackets and braces.
# Values will be pushed and popped and the stack will be
# examined to determine if the string is balanced.
# ===================================================

import sys


# Checks whether the input string is balanced
# param: input string
# returns True if string is balanced, otherwise returns False

class Stack:
    """
    This is the stack class containing an init function and other
    stack functions that will perform actions of the stack data
    structure.
    """
    def __init__(self):
        """
        initialization function will initialize the stack to empty
        (represented by an empty list) and the size to zero
        """
        self._stack = []
        self._stack_size = 0

    def get_stack(self):
        """
        getter get_stack will return the stack
        """
        return self._stack

    def push(self, val_param):
        """
        The push function will append or add a value to the top of a stack and increase size.
        """
        self._stack += [val_param]
        self._stack_size += 1
        return None

    def pop(self):
        """
        The pop function will take the last value of the stack, remove it and then return it.
        """
        pop_val = self._stack[self._stack_size - 1] # obtain the last value of the stack
        self._stack = self._stack[:self._stack_size - 1] # take the element off the stack
        self._stack_size -= 1
        return pop_val

    def top(self):
        """
        The top (peek) function will return the value of the element that has been most recently
        pushed to the stack.
        """
        return self._stack[self._stack_size - 1]

    def is_empty(self):
        """
        The empty function will return True if the stack is empty, False otherwise
        """
        if not self._stack:
            return True
        else:
            return False


def is_balanced(input_string):
    """
    This is the is_balanced function that will create a stack object and
    utilize the stack functions to determine if an input_ string has
    balanced parentheses, brackets and braces. If the stack's pop value
    does not correspond with its character match, the function will return
    False. If all the correct and corresponding values of the stack have
    been popped, the function will return True.
    """
    stack = Stack()  # create / instantiate stack object

    for i in input_string:  # iterate through string

        if i == "(" or i == "[" or i == "{":
            stack.push(i)  # push the left char onto the stack

        elif i == ")":  # if right parenthesis is reached
            if stack.is_empty() or stack.pop() != "(":  # see if stack is empty or not left parenthesis pops from stack
                return False

        elif i == "]": # if right bracket is reached
            if stack.is_empty() or stack.pop() != "[":  # see if stack is empty or not left bracket pops from stack
                return False

        elif i == "}": # if right brace is reached
            if stack.is_empty() or stack.pop() != "{":   # see if stack is empty or not left brace pops from stack
                return False

    return stack.is_empty() # if stack has been appropriately cleared and is empty, the function call will return true

"""if __name__ == '__main__':
    # get input string
    _input_string = sys.argv[1]  # DO NOT MODIFY
    balanced = is_balanced(_input_string)

    if balanced:
        print("The string {} is balanced".format(_input_string))
    else:
        print("The string {} is not balanced".format(_input_string))"""


if __name__ == '__main__':
    # get input string
    # _input_string = sys.argv[1]  # DO NOT MODIFY
    _input_string = ""
    balanced = is_balanced(_input_string)

    if balanced:
        print("The string {} is balanced".format(_input_string))
    else:
        print("The string {} is not balanced".format(_input_string))
