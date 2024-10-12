# Name: John-Francis Caccamo
# Date: 6 / 9 / 20

# Description: This is the word_count.py file which will
# ===================================================
# Implement a word counter that counts the number of
# occurrences of all the words in a file. Words from a sample
# text will be hashed to a hash map coupled with its count,
# represented by a tuple of key (word) : value (count). The
# top_words will subsequently call a heap sort on an array
# of key:values to sort the words in descending order based
# on count.
# Ultimately, the word counter will return the top X words, as indicated
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
    Returns the top `number` of words in a list of tuples of the form (word, count). The function
    will establish a hash map of word-count pairs representing the key-values. From the hash map,
    the tuples of the key-value pairs will be added to a set, the set will be converted to an
    array and a decreasing order heap sort function will be called to sort the key-value pairs
    largest to smallest.

    Args:
        source: the file name containing the text
        number: the number of top results to return (e.g. 5 would return the 5 most common words)
    Returns:
        A list of tuples of the form (word, count), sorted by most common word. (e.g. [("a", 23), ("the", 20), ("it", 10)])
    """

    keys = set()

    ht = HashMap(2500, hash_function_2)

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

    kv_arr = list(keys)  # obtain array of the set, hold the tuples of (key:value)s in kv_arr

    heap_sort(kv_arr)  # call the heap_sort function returning a set of k:v pairs in descending order

    tuple_key_value = []  # tuple_key_value will hold the top entries in list_of_keys, initialized to empty list

    for i in range(number):  # dependent on argument number
        tuple_key_value.append(kv_arr[i])  # append the top entries to tuple_key_value

    return tuple_key_value


def min_heapify(hm_arr, kv_len, i):
    """
    Min_heapify will determine the ordering of nodes and
    construct within a min_heap tree in order to create
    a sorted array in descending order.

    Will take the hash map array of key:value pairs, the length
    of the array and an index as parameters.
    """
    smallest = i  # initialize root to smallest
    l = 2 * i + 1  # left = 2 * i + 1
    r = 2 * i + 2  # right = 2 * i + 2

    if l < kv_len and hm_arr[l][1] < hm_arr[smallest][1]:  # if left is smaller than smallest (starting with root)
        smallest = l  # assign smallest to this left value

    if r < kv_len and hm_arr[r][1] < hm_arr[smallest][1]:  # if right is smaller than smallest (starting with root)
        smallest = r  # assign smallest to this right value

    if smallest != i:  # if smallest has changed
        hm_arr[i], hm_arr[smallest] = hm_arr[smallest], hm_arr[i]  # reassign root with a swap
        min_heapify(hm_arr, kv_len, smallest)  # min_heapify the root

    return


def heap_sort(hm_arr):
    """
    heap_sort will create the min_heap tree from an input array / list of hash_map key-value
    pairs and perform the swaps that create the sorted array descending order array.

    Will take in the hash map array of key:value pairs as a parameter.
    """
    kv_len = len(hm_arr)  # kv_len will represent the count of key-value pairs

    for i in range(kv_len // 2 - 1, -1, -1):  # build the minheap tree, starting at index to the left of the midpoint
        min_heapify(hm_arr, kv_len, i)  # in the array and thus this index will convert to the last node with children

    for i in range(kv_len - 1, 0, -1):  # extract each element from heap
        hm_arr[0], hm_arr[i] = hm_arr[i], hm_arr[0]  # start swapping beginning with the root and the last node
        min_heapify(hm_arr, i, 0)  # call min heapify to push smallest values down and out from tree, right in array

    return

# print(top_words("alice.txt",10))  # COMMENT THIS OUT WHEN SUBMITTING TO GRADESCOPE
