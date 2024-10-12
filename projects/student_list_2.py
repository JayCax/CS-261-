# Name: John-Francis Caccamo
# Date: 4 / 21 / 20
# student_list_3.py
# ===================================================
# Reimplementation of Pythons List -
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
        """if self._size == self._capacity:
            self._capacity *= 2
            new_array = np.empty([self._capacity], np.int16)
            new_array[:self._size] = self._list
            self._list = new_array
            np.delete(new_array, (0), axis=0)
        """

        if self._size == self._capacity:
            #self._capacity *= 2
            new_array = np.empty([self._capacity * 2], np.int16)
            for i in range(self._size):
                new_array[i] = self._list[i]
            self._list = new_array
            self._capacity *= 2
            np.delete(new_array, (0), axis=0)

    def append(self, val_param):
        # FIXME: You will write this function
        # if self._size == self._capacity:
        # self.increase_capacity()
        self.increase_capacity()
        self._list[self._size] = val_param
        self._size += 1
        # np.append(self._list, val)

    def pop(self):
        # FIXME: You will write this function
        # self._list.delete(self._list[-1])
        # numpy.delete(a, index)
        """np.delete(self._list, -1)
        self._size -= 1
        #self._list"""
        pop_val = self._list[self._size-1]
        self._list = self._list[:self._size-1]
        self._size -= 1
        return pop_val

    def insert(self, index_param, val_param):
        # FIXME: You will write this function
        if index_param - 1 > self._size or index_param < 0:
            return False
        self.increase_capacity()
        # np.insert(self._list, index, val)
        if index_param == 0:
            #np.r_[[val_param], self._list]
            #self._list[:index_param] = [val_param]
            #np.insert(self._list, 0, val_param, axis=0)
            #self._list = np.concatenate([[val_param], self._list])
            #self._list = self._list[-1]
            self._list = np.insert(self._list, index_param, val_param)
        else:
            self._list[index_param-1:index_param] = [val_param]
        self._size += 1

        """
        def insert(self, index, val):
        for i in range(0, len(self._list)):
            if index == i:
                self._list[i] = val
        """

    def remove(self, val_param):
        # FIXME: You will write this function
        # np.delete(self._list, val)
        """index_loc = 0
        for value in np.nditer(self._list):
            if value == val_param:
                self._list[index_loc:index_loc + 1] = []
                self._size -= 1
                return None
            index_loc += 1"""
        index_loc = 0
        for value in np.nditer(self._list):
            if value == val_param:
                self._list = np.delete(self._list, np.where(self._list == val_param))
                self._size -= 1
                return None
            index_loc += 1

    def clear(self):
        # FIXME: You will write this function
        # np.delete(self._list, (0), axis=0)
        #self._list = self._list[:]
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
    #print(s.pop()) # good
    s.insert(0, 0) # good
    s.insert(8,7)
    s.remove(0)
    #s.clear() # good
    print(s.count(2))
    #print(s.get(0)) # good
    print(s.get_array())
    print(s.get_capacity())

if __name__ == "__main__":
    main()
