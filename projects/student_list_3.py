# Name: John-Francis Caccamo
# Date: 4 / 21 / 20
# student_list_3.py
# Description:
# ===================================================
# Reimplementation of Python's List functions - reflected in custom
# functions that will change and manipulate numpy arrays
# ===================================================

import numpy as np


# StudentList class is our implementation of Python's List
class StudentList:
    def __init__(self):
        # creates an empty array of length 4, change the [4] to another value to make an
        # array of different length.
        self._list = np.empty([4], np.int16)
        self._capacity = 4
        self._size = 0

    def __str__(self):
        return str(self._list[:self._size])

    # You may want an internal function that handles resizing the array.
    # Dont modify get_list or get_capacity, they are for testing

    def get_list(self):
        return self._list[:self._size]

    def get_capacity(self):
        return self._capacity

    def increase_capacity(self):
        if self._size == self._capacity:
            new_array = np.empty([self._capacity * 2], np.int16)
            for i in range(self._size):
                new_array[i] = self._list[i]
            self._list = new_array
            self._capacity *= 2
            np.delete(new_array, (0), axis=0)

    def append(self, val_param):
        # FIXME: You will write this function
        self.increase_capacity()
        self._list[self._size] = val_param
        self._size += 1

    def pop(self):
        # FIXME: You will write this function
        pop_val = self._list[self._size - 1]
        self._list = self._list[:self._size - 1]
        self._size -= 1
        return pop_val

    def insert(self, index_param, val_param):
        # FIXME: You will write this function

        if index_param > self._size or index_param < 0:
            return False
        self.increase_capacity()
        if index_param == self._size:
            self.append(val_param)
        else:
            for i in range(self._size-1, index_param, -1):
                self._list[i + 1] = self._list[i]
            self._list[index_param + 1] = self._list[index_param]
            self._list[index_param] = val_param
            self._size += 1

        """if index_param - 1 >= self._size or index_param < 0:
            return False
        self.increase_capacity()
        #if index_param == self._size + 1:
            #self.append(val_param)
        if index_param == self._size - 1:
            self.append(val_param)
        else:
            for i in range(self._size, index_param - 1, -1):
                self._list[i + 1] = self._list[i]
            self._list[index_param] = val_param
        self._size += 1"""

        """if index_param - 1 >= self._size or index_param < 0:
            return False
        self.increase_capacity()
        new_array = np.empty([self._capacity], np.int16)
        for i in range(self._size, index_param, -1):
            new_array[i + 1] = self._list[i]
        new_array[index_param] = val_param
        for i in range(0, index_param):
            new_array[i] = self._list[i]
        self._list = new_array
        self._size += 1
        np.delete(new_array, (0), axis=0)"""

    def remove(self, val_param):
        # FIXME: You will write this function

        # index_loc = 0
        """for value in np.nditer(self._list):
            if value == val_param:
                self._list = np.delete(self._list, np.where(self._list == val_param))
                self._size -= 1
                new_array = np.empty([self._capacity], np.int16)
                for i in range(self._size):
                    new_array[i] = self._list[i]
                self._list = new_array
                np.delete(new_array, (0), axis=0)
                return None
            index_loc += 1"""

        index_loc = 0
        for value in self._list:
            if value == val_param:
                #self._list = np.delete(self._list, np.where(self._list == val_param))
                for i in range(index_loc, self._size-1):
                    self._list[i] = self._list[i + 1]
                self._size -= 1
                return None
            index_loc += 1

    def clear(self):
        # FIXME: You will write this function
        # np.delete(self._list, (0), axis=0)
        # self._list = self._list[:]
        self._list = np.empty([self._capacity], np.int16)
        self._size -= self._size

    def count(self, value_param):
        # FIXME: You will write this function
        count = 0
        for item in np.nditer(self._list):
            if item == value_param:
                count += 1
        return count

    def get(self, index_param):
        # FIXME: You will write this function
        return self._list[index_param]

    def get_array(self):
        return self._list


def main():
    s = StudentList()
    s.append(1)
    s.append(2)
    s.append(3)
    s.append(4)
    s.append(5)
    s.append(6)
    # print(s.pop()) # good
    s.insert(0, 0)  # good

    s.insert(7, 69)
    s.insert(0, -1)
    s.remove(0) # good
    s.insert(0, 6999)
    # s.clear() # good
    # print(s.count(2))
    # print(s.get(0)) # good
    print(s.get_array())
    print(s._size)
    print(s.get_capacity())

    s2 = StudentList()
    s2.insert(0, 50)
    s2.insert(0, 50)
    s2.insert(0, 50)
    s2.insert(0, 50)
    #s2.remove(50)
    print(s2.get_array())
    print(s2._size)
    print(s2.get_capacity())


if __name__ == "__main__":
    main()
