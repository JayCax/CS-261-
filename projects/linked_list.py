# Name: John-Francis Caccamo
# Date: 5 / 5 / 20

# Description: This is the linked_list.py file containing functions
# that will manipulate, add and remove values in linked list
# and circular doubly linked lists ADTs
# ===================================================
# Linked list exploration
# Part 1: implement the deque and bag ADT with a Linked List
# Part 2: implement the deque ADT with a CircularlyDoubly-
# Linked List
# ===================================================


'''
**********************************************************************************
Part1: Deque and Bag implemented with Linked List

Each linked list will have a head and tail sentinel node
**********************************************************************************
'''


class SLNode:
    def __init__(self):
        self.next = None
        self.data = None


class LinkedList:
    def __init__(self, start_list=None):
        """
        Initializes a linked list with a head and tail node with None data
        """
        self.head = SLNode()
        self.tail = SLNode()
        self.head.next = self.tail
        # populate list with initial set of nodes (if provided)
        if start_list is not None:
            for data in start_list:
                self.add_back(data)

    def __str__(self):
        """
        Returns a human readable string of the list content of the form
        [value1 -> value2 -> value3]

        An empty list should just return []

        Returns:
            The string of the human readable list representation
        """
        out = '['
        if self.head.next != self.tail:
            cur = self.head.next.next
            out = out + str(self.head.next.data)
            while cur != self.tail:
                out = out + ' -> ' + str(cur.data)
                cur = cur.next
        out = out + ']'
        return out

    def add_link_before(self, data, index):
        """
        Adds a new link containing data and inserts it before the link at index.
        If index is 0, it inserts at the beginning of the list.

        There will be a check determining if an index is negative in which case an
        IndexError will be thrown. If the insertion index is 0, the function  will call
        the add_front method. Otherwise, iteration will proceed from the head
        until the node previous the insertion point, add the next node / link with
        the remaining values of the linked list and reassign the next pointer.

        Args:
            data: The data the new node will contain
            index: The index of the node that will immediately follow the newly added node
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # FIXME: Complete this function

        if index < 0:  # if index is negative
            raise IndexError("Index Out of Bounds")  # raise the exception

        elif index == 0:  # adding at the first index will call the add_front function
            self.add_front(data)

        else:
            prev_ptr = self.head  # prev pointer will update to before the insertion position

            for node in range(index):  # iterate to before insertion point
                if prev_ptr.next is self.tail:  # check to determine if we have reached end of linked list
                    raise IndexError("Index Out of Bounds")  # raise the exception if next value is the sentinel
                prev_ptr = prev_ptr.next  # update prev_ptr

            new_link.next = prev_ptr.next  # make all of new_link's subsequent values prev_ptr's subsequent values
            prev_ptr.next = new_link  # update the linked list with the new link

        return

    def remove_link(self, index):
        """
        Removes the link at the location specified by index

        There will be a check determining if an index is negative in which case an
        IndexError will be thrown. If the insertion index is 0, the function  will call
        the remove_front method. Otherwise, iteration will proceed from the head
        until the node previous the one to be removed, remove the next node and
        reassign the pointer.

        Args:
            Index: The index of the node that will be removed
        """

        # FIXME: Write this function

        if index < 0:  # if index is negative
            raise IndexError("Index Out of Bounds")  # raise the exception

        elif index == 0:  # removing at the first index will call the remove_front function
            self.remove_front()

        else:
            prev_ptr = self.head  # prev pointer will update to before the insertion position

            for node in range(index):  # iterate to before removal point
                if prev_ptr.next is self.tail:  # check to determine if we have reached end of linked list
                    raise IndexError("Index Out of Bounds")  # raise the exception if next value is the sentinel
                prev_ptr = prev_ptr.next  # update prev_ptr

            prev_ptr.next = prev_ptr.next.next  # cut out the link to be removed by reassigning the next pointer

        return

    def add_front(self, data):
        """
        Adds a new node after the head that contains data and will adjust
        self.head.next to this new, inserted front node.

        Args:
            data: The data the new node will contain
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # FIXME: Complete this function

        new_link.next = self.head.next  # make all of new_link's subsequent values the head's subsequent values
        self.head.next = new_link  # reassign the new head.next pointer to the new_link

        return

    def add_back(self, data):
        """
        Adds a new node before the tail that contains data. Will iterate to
        the end of the linked list before tail and insert the new node.

        Args:
            data: The data the new node will contain
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # FIXME: Complete this function

        if self.head.next == self.tail:  # check to see if the linked list has no data nodes
            new_link.next = self.tail  # set new_link's next pointer to the tail
            self.head.next = new_link  # update the head pointer to the new link

        else:
            node_ptr = self.head  # set node_ptr to the head

            while node_ptr.next is not self.tail:  # iterate through the linked list to before tail
                node_ptr = node_ptr.next

            new_link.next = self.tail  # set new_link's next pointer to the tail
            node_ptr.next = new_link  # update the ll with the new_link inserted before the tail

        return

    def get_front(self):
        """
        Returns the data in the element at the front of the list. Will return
        None in an empty list.

        Will return the data held in self.head.next.

        Returns:
            The data in the node at index 0 or None if there is no such node
        """

        # FIXME: Write this function

        if self.head.next.data is None:  # check to determine if the list is empty
            return None  # and return None

        return self.head.next.data  # otherwise return the data of the first node in linked list

    def get_back(self):
        """
        Returns the data in the element at the end of the list. Will return
        None in an empty list.

        Will iterate to node before self.tail and return the data held.

        Returns:
            The data in the node at last index of the list or None if there is no such node
        """

        # FIXME: Write this function

        if self.head.next is self.tail:  # check to determine if there are no nodes ll, will simply return
            return None

        ll_ptr = self.head  # assign ll_ptr to the head pointer

        while ll_ptr.next is not self.tail:  # loop to the last node and value of the linked list
            ll_ptr = ll_ptr.next

        return ll_ptr.data  # return the data of that last link

    def remove_front(self):
        """
        Removes the first element of the list. Will not remove the tail.

        Will remove the value matching self.head.next and reform links to
        reflect the new next node in the linked list.
        """

        # FIXME: Write this function

        if self.head.next is self.tail:  # if there are no nodes in the linked list, simply return
            return

        self.head.next = self.head.next.next  # update the head pointer's next value to the second value in ll

        return

    def remove_back(self):
        """
        Removes the last element of the list. Will not remove the head.

        Will iterate to 2 nodes away from the self.tail and make this second
        to last value the new final node containing data before self.tail.
        """

        # FIXME: Write this function

        if self.head.next is self.tail:  # check if the linked list is empty
            return  # if there are no nodes in the ll, simply return

        ll_ptr = self.head  # assign ll_ptr to the head pointer

        while ll_ptr.next.next is not self.tail:  # iterate to the second to last node with data in the ll
            ll_ptr = ll_ptr.next

        ll_ptr.next = ll_ptr.next.next  # remove the last link by reassigning the next pointer to the tail

        return

    def is_empty(self):
        """
        Checks if the list is empty

        If there are no nodes in the linked list, the function will return True.

        Returns:
            True if the list has no data nodes, False otherwise
        """

        # FIXME: Write this function

        if self.head.next is self.tail:  # if there are no nodes and head.next pointer is the tail
            return True

        return False  # if there are nodes in the ll, return False

    def contains(self, value):
        """
        Checks if any node contains value

        The function will iterate through the linked list to find
        node data matching the value parameter. If a node's data matches, a boolean
        will be updated to True, the iteration will cease and
        the function will return True.

        Args:
            value: The value to look for

        Returns:
            True if value is in the list, False otherwise
        """

        # FIXME: Write this function

        if self.head.next is self.tail:  # if there are no nodes and head.next pointer is the tail
            return  # return out of the function

        data_found = False  # variable that will hold the boolean value of the data occurring in ll
        ll_ptr = self.head  # pointer starting at head

        while ll_ptr is not self.tail:  # iterate to the end of the linked list
            if value == ll_ptr.data:  # if data has been found
                data_found = True  # change the boolean
                break  # and break from the loop
            ll_ptr = ll_ptr.next  # else, continue iteration

        return data_found  # return the boolean

    def remove(self, value):
        """
        Removes the first instance of an element from the list

        The function will iterate through the linked list to find
        node data matching the value parameter. If a node's data matches, the
        node will be removed and iteration through the linked list will stop.

        Args:
            value: the value to remove
        """

        # FIXME: Write this function

        curr_ptr = self.head  # set current pointer at head of ll

        while curr_ptr is not self.tail:  # while the end of the ll hasn't been reached
            if value == curr_ptr.data:  # if the value to be removed has been found
                prev_ptr.next = curr_ptr.next  # remove the node matching the value parameter at curr_ptr
                return  # exit from function
            prev_ptr = curr_ptr  # set prev_ptr to current pointer
            curr_ptr = curr_ptr.next  # make current pointer point to the next value in the ll

        return


'''
**********************************************************************************
Part 2: Deque implemented with CircularlyDoublyLinked List

Each node will have both a previous and a next pointer and start and end 
at the sentinel node
**********************************************************************************
'''


class DLNode:
    def __init__(self):
        self.next = None
        self.prev = None
        self.data = None


class CircularList:
    def __init__(self, start_list=None):
        """
        Initializes a linked list with a single sentinel node containing None data
        """
        self.sentinel = DLNode()
        self.sentinel.next = self.sentinel
        self.sentinel.prev = self.sentinel

        # populate list with initial set of nodes (if provided)
        if start_list is not None:
            for data in start_list:
                self.add_back(data)

    def __str__(self):
        """
        Returns a human readable string of the list content of the form
        [value1 <-> value2 <-> value3]

        An empty list should just print []

        Returns:
            The string of the human readable list representation
        """
        out = '['
        if self.sentinel.prev != self.sentinel:
            cur = self.sentinel.next.next
            out = out + str(self.sentinel.next.data)
            while cur != self.sentinel:
                out = out + ' <-> ' + str(cur.data)
                cur = cur.next
        out = out + ']'
        return out

    def add_link_before(self, data, index):
        """
        Adds a new link containing data and inserts it before the link at index.
        If index is 0, it inserts at the beginning of the list.

        There will be a check determining if an index is negative in which case an
        IndexError will be thrown. If the insertion index is 0, the function  will call
        the add_front method. Otherwise, iteration will proceed from the sentinel
        until the node previous the insertion point, add the next node / link with the
        remaining values of the circular doubly linked list and
        reassign next and previous pointers.

        Args:
            data: The data the new node will contain
            index: The index of the node that will immediately follow the newly added node
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # FIXME: Complete this function

        if index < 0:  # if index is negative
            raise IndexError("Index Out of Bounds")  # raise the exception

        if index == 0:  # adding at the first index will call the add_front function
            self.add_front(data)

        else:
            cd_ll_ptr = self.sentinel  # create pointer pointing to sentinel

            for node in range(index):  # iterate through the cd ll
                if cd_ll_ptr.next is self.sentinel:  # if the cd ll has been circled
                    raise IndexError("Index Out of Bounds")  # raise the exception
                cd_ll_ptr = cd_ll_ptr.next  # continue iterating

            new_link.next = cd_ll_ptr.next  # set the new link's next pointer to the pointer's
            new_link.prev = cd_ll_ptr  # new links previous pointer to the node the iteration stopped at
            cd_ll_ptr.next.prev = new_link  # inserting the new link and updating the pointers of
            cd_ll_ptr.next = new_link  # the cd_ll_pointer

            return

    def remove_link(self, index):
        """
        Removes the link at the location specified by index

        There will be a check determining if an index is negative in which case an
        IndexError will be thrown. If the insertion index is 0, the function  will call
        the remove_front method. Otherwise, iteration will proceed from the sentinel
        until the node previous the one to be removed, remove the next node and
        reassign next and previous pointers.

        Args:
            Index: The index of the node that will be removed
        """

        # FIXME: Write this function

        if index < 0:  # if index is negative
            raise IndexError("Index Out of Bounds")  # raise the exception

        elif index == 0:  # removing at the first index will call the remove_front function
            self.remove_front()

        else:
            cd_ll_ptr = self.sentinel  # create pointer pointing to sentinel

            for node in range(index):  # iterate through the cd ll
                if cd_ll_ptr.next is self.sentinel.prev:  # if the cd ll has been circled
                    raise IndexError("Index Out of Bounds")  # raise the exception
                cd_ll_ptr = cd_ll_ptr.next  # continue iterating

            cd_ll_ptr.next.next.prev = cd_ll_ptr  # set the value 2 spaces ahead previous to the cd_ll_ptr
            cd_ll_ptr.next = cd_ll_ptr.next.next  # set the next pointer to the node 2 spaces ahead

        return

    def add_front(self, data):
        """
        Adds a new node at the beginning of the list that contains data and will adjust
        self.sentinel.next to accommodate this new node.

        Args:
            data: The data the new node will contain
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # FIXME: Complete this function

        new_link.next = self.sentinel.next  # set the new_link's next ptr to the sentinel's next
        new_link.prev = self.sentinel  # set the new_link's previous ptr to the sentinel
        self.sentinel.next.prev = new_link  # update with the new link inserted at the front via
        self.sentinel.next = new_link  # updating sentinel's pointers

        return

    def add_back(self, data):
        """
        Adds a new node at the end of the list that contains data and will adjust
        self.sentinel.prev to accommodate this new node.

        Args:
            data: The data the new node will contain
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # FIXME: Complete this function

        new_link.next = self.sentinel  # set the new_link's next ptr to the sentinel
        new_link.prev = self.sentinel.prev  # set the new_link's previous ptr to that of the sentinel
        self.sentinel.prev.next = new_link  # update with the new link inserted at the back and updating
        self.sentinel.prev = new_link  # sentinel's pointers

        return

    def get_front(self):
        """
        Returns the data in the element at the front of the list. Will return
        None in an empty list. Will return the data held in self.sentinel.next.

        Returns:
            The data in the node at index 0 or None if there is no such node
        """

        # FIXME: Write this function

        if self.sentinel.next is self.sentinel:  # check to determine if the cd ll is empty - will return None
            return None

        return self.sentinel.next.data  # otherwise return the data held in next node with respect to sentinel

    def get_back(self):
        """
        Returns the data in the element at the end of the list. Will return
        None in an empty list. Will return the data held in self.sentinel.prev.

        Returns:
            The data in the node at last index of the list or None if there is no such node
        """

        # FIXME: Write this function

        if self.sentinel.prev is self.sentinel:  # check to determine if the cd ll is empty - will return None
            return None

        return self.sentinel.prev.data  # otherwise return the data held in previous node with respect to sentinel

    def remove_front(self):
        """
        Removes the first element of the list. Will not remove the tail.

        Will remove the value matching self.sentinel.next and reform links to
        reflect the new self.sentinel.next node in the circular doubly linked list.
        """

        # FIXME: Write this function

        if self.sentinel.next is self.sentinel:  # check to determine if the cd ll is empty - will simply return
            return

        self.sentinel.next.next.prev = self.sentinel  # remove the first node in the cd ll by setting the ptr
        self.sentinel.next = self.sentinel.next.next  # 2 nodes ahead as the next node from sentinel

        return

    def remove_back(self):
        """
        Removes the last element of the list. Will not remove the head.

        Will remove the value matching self.sentinel.prev and reform links to
        reflect the new self.sentinel.prev node in circular doubly linked list.
        """

        # FIXME: Write this function

        if self.sentinel.prev is self.sentinel:  # check to determine if the cd ll is empty - will simply return
            return

        self.sentinel.prev.prev.next = self.sentinel  # remove the last node in the cd ll by setting the ptr
        self.sentinel.prev = self.sentinel.prev.prev  # 2 nodes previous as sentinel's previous node

        return

    def is_empty(self):
        """
        Checks if the list is empty

        If there are no nodes in the circular doubly linked list, the function will return True.

        Returns:
            True if the list has no data nodes, False otherwise
        """

        # FIXME: Write this function

        if self.sentinel.next is self.sentinel and self.sentinel.prev is self.sentinel:  # if no nodes in the cd ll
            return True

        return False

    def contains(self, value):
        """
        Checks if any node contains value

        The function will iterate through the circular doubly linked list to find
        node data matching the value parameter. If a node's data matches, a boolean
        will be updated to True, the iteration will cease and
        the function will return True.

        Args:
            value: The value to look for

        Returns:
            True if value is in the list, False otherwise
        """

        # FIXME: Write this function

        if self.sentinel.next is self.sentinel: # if there are no nodes in the cd ll
            return

        data_found = False  # variable that will hold the boolean value of the data occurring in ll
        cd_ll_ptr = self.sentinel.next  # start at the first value from sentinel

        while cd_ll_ptr is not self.sentinel:  # while the cd ll hasn't been fully circled
            if value == cd_ll_ptr.data:  # if the node with data matching the value parameter has been found
                data_found = True  # update data found
                break  # break from the loop once found
            cd_ll_ptr = cd_ll_ptr.next  # else, proceed with iteration

        return data_found  # return the value of the boolean

    def remove(self, value):
        """
        Removes the first instance of an element from the list

        The function will iterate through the circular doubly linked list to find
        node data matching the value parameter. If a node's data matches, the
        node will be removed and iteration through the circular doubly linked list
        will stop.

        Args:
            value: the value to remove
        """

        # FIXME: Write this function

        if self.sentinel.next is self.sentinel and self.sentinel.prev is self.sentinel:  # check if cd ll is empty
            return

        cd_ll_ptr = self.sentinel.next  # start at the first value from sentinel

        while cd_ll_ptr is not self.sentinel:  # while the cd ll hasn't been fully circled
            if value == cd_ll_ptr.data:  # if the node with data matching the value parameter has been found
                cd_ll_ptr.prev.next = cd_ll_ptr.next  # set the node's previous pointer to the next
                cd_ll_ptr.next.prev = cd_ll_ptr.prev  # set the next node's next pointer to the previous node
                return  # exit function
            cd_ll_ptr = cd_ll_ptr.next  # else, proceed iterating

        return

    def circularListReverse(self):
        """
        Reverses the order of the links. It must not create any additional new links to do so.
        (e.g. you cannot call DLNode()). If the list printed by following next was 0, 1, 2, 3,
        after the call it will be 3,2,1,0

        This function will work backwards switching pointers starting at self.sentinel.previous,
        cumulating with self.sentinel.next and self.sentinel.prev being swapped.
        """

        # FIXME: Write this function

        if self.sentinel.next is self.sentinel and self.sentinel.prev is self.sentinel:  # check if cd ll is empty
            return

        curr_ptr = self.sentinel.prev  # set the current pointer to the previous value w/ respect to sentinel

        while curr_ptr is not self.sentinel:  # iterate backwards through the cd ll
            curr_ptr.next, curr_ptr.prev = curr_ptr.prev, curr_ptr.next  # swap next and current pointer values
            curr_ptr = curr_ptr.next  # iterate backwards through the cd ll

        self.sentinel.next, self.sentinel.prev = self.sentinel.prev, self.sentinel.next  # update sentinel's pointers

        return
