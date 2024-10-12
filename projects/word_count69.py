# Name: John-Francis Caccamo
# Date: 6 / 9 / 20

# Description: This is the word_count.py file which will
# ===================================================
# Implement a word counter that counts the number of
# occurrences of all the words in a file. Words from a sample
# text will be hashed to a hash map coupled with its count.
# The word counter will return the top X words, as indicated
# by the user.
# ===================================================

import re
from hash_map import HashMap

"""
This is the regular expression used to capture words. It could probably be endlessly
tweaked to catch more words, but this provides a standard we can test against, so don't
modify it for your assignment submission.
"""
rgx = re.compile("(\w[\w']*\w|\w)")

def hash_function_2(key):
    """
    This is a hash function that can be used for the hashmap.
    """

    hash = 0
    index = 0
    for i in key:
        hash = hash + (index + 1) * ord(i)
        index = index + 1
    return hash

def top_words(source, number):
    """
    Takes a plain text file and counts the number of occurrences of case insensitive words.
    Returns the top `number` of words in a list of tuples of the form (word, count).

    Args:
        source: the file name containing the text
        number: the number of top results to return (e.g. 5 would return the 5 most common words)
    Returns:
        A list of tuples of the form (word, count), sorted by most common word. (e.g. [("a", 23), ("the", 20), ("it", 10)])
    """

    keys = set()

    ht = HashMap(2500,hash_function_2)

    # This block of code will read a file one word as a time and
    # put the word in `w`. It should be left as starter code.
    with open(source) as f:
        for line in f:
            words = rgx.findall(line)

            for w in words:

                # FIXME: Complete this function
                w = w.lower()  # convert each word to lower case

                if not ht.get(w):  # if the word does not exist in the hash map
                    ht.put(w, 1)  # initialize the word with the value 1
                else:  # if the word has been encountered and exists in the hash map
                    update_value = ht.get(w) + 1  # access value and increment it
                    ht.put(w, update_value)  # replace key with the updated value

    for linked_list in ht.return_buckets():  # for each linked list in the hash map
        if linked_list.head:  # if there are values
            ll_ptr = linked_list.head  # create a pointer
            while ll_ptr:  # while the end of the linked list has not been reached
                keys.add((ll_ptr.key, ll_ptr.value))  # add the key-value tuple
                ll_ptr = ll_ptr.next  # proceed with iteration


    #print(keys)

    #list_of_keys = []

    list_of_keys = list(keys)  # obtain list of the set

    #list_of_keys.sort(key=lambda tup: tup[1], reverse=True)

    heapSort(list_of_keys)

    #sorted_keys = hm_sort(list_of_keys)

    #sorted_keys.reverse()

    tuple_key_value = []

    for i in range(number):
        tuple_key_value.append(list_of_keys[i])
        
    return tuple_key_value



def hm_sort(array):

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0][1]
        for x in array:
            if x[1] < pivot:
                less.append(x)
            elif x[1] == pivot:
                equal.append(x)
            elif x[1] > pivot:
                greater.append(x)

        return hm_sort(less) + equal + hm_sort(greater)

    else:
        return array

"""def hm_sort(sqc):
    def down_heap(sqc, k, n):
        parent = sqc[k][1]

        while 2*k+1 < n:
            child = 2*k+1
            if child+1 < n and sqc[child][1] < sqc[child+1][1]:
                child += 1
            if parent >= sqc[child][1]:
                break
            sqc[k] = sqc[child]
            k = child
        sqc[k] = parent

    size = len(sqc)

    for i in range(size//2-1, -1, -1):
        down_heap(sqc, i, size)

    for i in range(size-1, 0, -1):
        sqc[0], sqc[i] = sqc[i], sqc[0]
        down_heap(sqc, 0, i)"""


def heapify(arr, n, i):
    smallest = i # Initialize smallest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2

    if l < n and arr[l][1] < arr[smallest][1]:  # if left is smaller than smallest (starting with root)
        smallest = l  # assign smallest to this left value

    if r < n and arr[r][1] < arr[smallest][1]:  # if right is smaller than smallest (starting with root)
        smallest = r  # assign smallest to this right value

    if smallest != i:  # if smallest has changed
        arr[i], arr[smallest] = arr[smallest], arr[i]  # recreate root with a swap
        heapify(arr, n, smallest)  # heapify the root

    # The main function to sort an array of given size


def heapSort(arr):
    n = len(arr)

    # Build a minheap.
    for i in range(n // 2 - 1, -1, -1):  #
        heapify(arr, n, i)

        # One by one extract elements
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # swap
        heapify(arr, i, 0)

#print(top_words("alice.txt",10))  # COMMENT THIS OUT WHEN SUBMITTING TO GRADESCOPE