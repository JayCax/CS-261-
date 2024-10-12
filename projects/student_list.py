# Name: John-Francis Caccamo
# Date: 4 / 21 / 20
# student_list_3.py
# Description:
# ===================================================
# This is the student_list.py file containing
# reimplementation of Python's List functions - reflected in custom
# functions mimicking Python list
# functions that will resize, change, manipulate and
# reassign numpy arrays. These restructured functions
# include append, pop, insert, remove, clear, count and get
# ===================================================

import numpy as np


# StudentList class is our implementation of Python's List

class StudentList:
    """
    The StudentList class will have init function, getters
    of member variables, a function increase_capacity that
    will resize the array, and append, pop, insert, remove,
    clear, count, and get functions that will mimic such
    Python built-in list functions.
    """

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
        """
        getter get_list will return the numpy array
        """
        return self._list[:self._size]

    def get_capacity(self):
        """
        getter get_capacity will return the numpy array's capacity
        """
        return self._capacity

    def increase_capacity(self):
        """
        This is the increase_capacity function containing a check
        determining if the array size is equal to the capacity.
        If it is, the numpy array will will be doubled
        accordingly to accommodate new values.
        """
        if self._size == self._capacity: # if the array capacity has been reached
            new_array = np.empty([self._capacity * 2], np.int16) # make temp, new array of doubled size

            for i in range(self._size): # copy original array values into the new array with for loop
                new_array[i] = self._list[i]

            self._list = new_array # reassign self._list to the new, larger array
            self._capacity *= 2 # double member variable capacity
            np.delete(new_array, (0), axis=0) # delete the temporary array

        return None

    def append(self, val_param):
        """
        The append function will utilize the current array size
        to create a new index to hold the new, appended value
        """
        self.increase_capacity()  # sufficient capacity check
        self._list[self._size] = val_param  # appending at last array position
        self._size += 1
        return None

    def pop(self):
        """
        The pop function will pop, remove and return the
        last value of the numpy array.
        """
        pop_val = self._list[self._size - 1]  # pop_val will hold the last value of array
        self._list = self._list[:self._size - 1]  # removing the last value of array
        self._size -= 1
        return pop_val

    def insert(self, index_param, val_param):
        """
        The insert function will take a index and value parameter. if the index is
        a valid index in the array, the array will insert the value based on where
        the index param indicates.
        """
        if index_param > self._size or index_param < 0:  # check if index_ param is valid
            return False
        self.increase_capacity()  # sufficient capacity check

        if index_param == self._size:  # if index_param is equal to self._size or the last
            self.append(val_param)  # index of the array, simply append
        else:
            for i in range(self._size - 1, index_param, -1):  # increment down from last index to index_param
                self._list[i + 1] = self._list[i]  # push the values into next index

            self._list[index_param + 1] = self._list[index_param]  # push the value currently in insert index
            self._list[index_param] = val_param  # insert the new value
            self._size += 1

            return None

    def remove(self, val_param):
        """
        The remove function will find the first matching value corresponding
        to a value parameter and remove it.
        """
        index_loc = 0  # counter variable
        for value in self._list:  # iterate thru array
            if value == val_param:  # if the value matches the value parameter
                for i in range(index_loc, self._size - 1):  # iterate down from end of array to remove val index
                    self._list[i] = self._list[i + 1]  # push the values down

                self._size -= 1  # reduce size
                return None
            index_loc += 1  # keep iterating through array if value has not been encountered

        return None

    def clear(self):
        """
        The clear function will reinitialize the numpy array to an empty array
        """
        self._list = np.empty([self._capacity], np.int16) # initiaze self._list to an empty array
        self._size -= self._size  # clear the size of the array
        return None

    def count(self, value_param):
        """
        The count function will take a value parameter and count how many times
        that value occurs in the array, returning this count.
        """
        val_counter = 0  # initialize count to zero
        for value in np.nditer(self._list):
            if value == value_param:  # if the value equals the value parameter
                val_counter += 1  # increment count

        return val_counter

    def get(self, index_param):
        """
        This function will return the value held at specific index, passed in as
        a parameter.
        """
        return self._list[index_param]


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
    s.remove(0)  # good
    s.insert(0, 6999)
    # s.clear() # good
    # print(s.count(2))
    # print(s.get(0)) # good
    print(s.get_list())
    print(s._size)
    print(s.get_capacity())

    s2 = StudentList()
    s2.insert(0, 50)
    s2.insert(0, 50)
    s2.insert(0, 50)
    s2.insert(0, 50)
    # s2.remove(50)
    print(s2.get_list())
    print(s2._size)
    print(s2.get_capacity())


if __name__ == "__main__":
    main()