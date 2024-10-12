import numpy as np

#test_list = np.array([1, 2, 3, 4, 5])

#test_list.tolist()
"""
test_list = [1, 2, 3, 4, 5]


def append(input_list, input_value):
    input_list[len(input_list):] = [input_value]
    return input_list


append(test_list, 6)

print(test_list)"""

test_list = np.array([1, 2, 3, 4, 5])

def append(input_list, input_value):
    input_list[len(input_list):] = [input_value]

append(test_list, 6)

print(test_list)
