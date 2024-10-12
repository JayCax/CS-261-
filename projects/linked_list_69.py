# linked_list_69.py
# ===================================================
# Linked list exploration
# Part 1: implement the deque and bag ADT with a Linked List
# Part 2: implement the deque ADT with a CircularlyDoubly-
# Linked List
# ===================================================


'''
**********************************************************************************
Part1: Deque and Bag implemented with Linked List
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

        Args:
            data: The data the new node will contain
            index: The index of the node that will immediately follow the newly added node
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # FIXME: Complete this function

        if index < 0:
            raise Exception("Index Out of Bounds")
        if index == 0:
            self.add_front(data)
        else:
            prev_ptr = self.head
            for node in range(index):
                if prev_ptr.next is self.tail:
                    raise Exception("Index Out of Bounds")
                prev_ptr = prev_ptr.next
            new_link.next = prev_ptr.next
            prev_ptr.next = new_link
        return


    def remove_link(self, index):
        """
        Removes the link at the location specified by index
        Args:
            Index: The index of the node that will be removed
        """

        # FIXME: Write this function

        """if index < 0:
            return
        if index == 0:
            self.head = self.head.next
        else:
            prev_ptr = self.head
            for node in range(index - 1):
                if prev_ptr:
                    prev_ptr = prev_ptr.next
                else:
                    break
            if prev_ptr is None:
                return
            if prev_ptr.next == self.tail:
                self.tail = prev_ptr

            if prev_ptr.next is None:
                return

            prev_ptr.next = prev_ptr.next.next"""

        if index < 0:
            raise Exception("Index Out of Bounds")
        if index == 0:
            self.remove_front()
        else:
            prev_ptr = self.head
            for node in range(index):
                if prev_ptr.next.next is self.tail:
                    raise Exception("Index Out of Bounds")
                prev_ptr = prev_ptr.next
           #if prev_ptr.next is None or prev_ptr is self.tail:
                #raise Exception("Index Out of Bounds")
            prev_ptr.next = prev_ptr.next.next
        return

    def add_front(self, data):
        """
        Adds a new node after the head that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # FIXME: Complete this function

        new_link.next = self.head.next
        self.head.next = new_link
        return


    def add_back(self, data):
        """
        Adds a new node before the tail that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = SLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # FIXME: Complete this function

        if self.head.next == self.tail:
            new_link.next = self.tail
            self.head.next = new_link
        else:
            node_ptr = self.head
            while node_ptr.next != self.tail:
                node_ptr = node_ptr.next
            new_link.next = self.tail
            node_ptr.next = new_link
        return


    def get_front(self):
        """
        Returns the data in the element at the front of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at index 0 or None if there is no such node
        """

        # FIXME: Write this function

        if self.head.next.data is None:
            return None
        return self.head.next.data

    def get_back(self):
        """
        Returns the data in the element at the end of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at last index of the list or None if there is no such node
        """

        # FIXME: Write this function

        ll_ptr = self.head
        while ll_ptr.next.data is not None:
            ll_ptr = ll_ptr.next
        return ll_ptr.data

    def remove_front(self):
        """
        Removes the first element of the list. Will not remove the tail.
        """

        # FIXME: Write this function

        if self.head.next == self.tail:
            return
        #ll_ptr = self.head
        #ll_ptr = ll_ptr.next.next
        self.head.next = self.head.next.next

    def remove_back(self):
        """
        Removes the last element of the list. Will not remove the head.
        """

        # FIXME: Write this function

        ll_ptr = self.head
        while ll_ptr.next.next is not self.tail:
            ll_ptr = ll_ptr.next
        ll_ptr.next = ll_ptr.next.next


    def is_empty(self):
        """
        Checks if the list is empty

        Returns:
            True if the list has no data nodes, False otherwise
        """

        # FIXME: Write this function

        if self.head.next is self.tail:
            return True
        return False

    def contains(self, value):
        """
        Checks if any node contains value

        Args:
            value: The value to look for

        Returns:
            True if value is in the list, False otherwise
        """

        # FIXME: Write this function

        data_found = False
        ll_ptr = self.head

        while ll_ptr is not self.tail:
            if value == ll_ptr.data:
                data_found = True
                break
            ll_ptr = ll_ptr.next
        return data_found

    def remove(self, value):
        """
        Removes the first instance of an element from the list

        Args:
            value: the value to remove
        """

        # FIXME: Write this function

        cur_ptr = self.head
        while cur_ptr is not self.tail:
            if value == cur_ptr.data:
                prev_ptr.next = cur_ptr.next
                return None
            prev_ptr = cur_ptr
            cur_ptr = cur_ptr.next


'''
**********************************************************************************
Part 2: Deque implemented with CircularlyDoublyLinked List
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

        Args:
            data: The data the new node will contain
            index: The index of the node that will immediately follow the newly added node
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # FIXME: Complete this function

        if index < 0:
            raise Exception("Index Out of Bounds")
        if index == 0:
            """new_link.next = self.sentinel.next
            self.sentinel.next.prev = new_link
            new_link.prev = self.sentinel
            self.sentinel.next = new_link"""
            self.add_front(data)
        else:
            cd_ll_ptr = self.sentinel

            for node in range(index):
                if prev_ptr.next is self.tail:
                    raise Exception("Index Out of Bounds")
                cd_ll_ptr = cd_ll_ptr.next
            #if cd_ll_ptr is None:
                #return
            new_link.next = curr_ptr.next
            new_link.prev = curr_ptr
            curr_ptr.next.prev = new_link
            curr_ptr.next = new_link
            return


    def remove_link(self, index):
        """
        Removes the link at the location specified by index
        Args:
            Index: The index of the node that will be removed
        """

        # FIXME: Write this function

        """if index < 0:
            return False
        for i in range(index):
            self.head = self.head.next
        self.head.next.next.prev = self.head
        self.head = self.head.next.next"""

        if index < 0:
            return
        if index == 0:
            self.head = self.head.next
        else:
            prev_ptr = self.head
            for node in range(index - 1):
                if prev_ptr:
                    prev_ptr = prev_ptr.next
                else:
                    break
            if prev_ptr is None:
                return
            prev_ptr.next = prev_ptr.next.next
            prev.ptr.next.next.prev = prev_ptr.next
        return



    def add_front(self, data):
        """
        Adds a new node at the beginning of the list that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # FIXME: Complete this function

        if self.sentinel.next is self.sentinel:
            new_link.next = self.sentinel
            new_link.prev = self.sentinel
            self.sentinel.prev = new_link
            self.sentinel.next = new_link

        new_link.next = self.sentinel.next
        self.sentinel.next.prev = new_link
        new_link.prev = self.sentinel
        self.sentinel.next = new_link

    def add_back(self, data):
        """
        Adds a new node at the end of the list that contains data

        Args:
            data: The data the new node will contain
        """
        new_link = DLNode()  # initialize a new link
        new_link.data = data  # set new_link data

        # FIXME: Complete this function

        cd_ll_ptr = self.sentinel
        while cd_ll_ptr is not None:
            cd_ll_ptr = cd_ll_ptr.next
        new_link.next = self.sentinel.next
        self.sentinel.prev = new_link
        cd_ll_ptr.next = new_link
        new_link.prev = cd_ll_ptr

    def get_front(self):
        """
        Returns the data in the element at the front of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at index 0 or None if there is no such node
        """

        # FIXME: Write this function

        if self.head.data is None:
            return None
        return self.head.data


    def get_back(self):
        """
        Returns the data in the element at the end of the list. Will return
        None in an empty list.

        Returns:
            The data in the node at last index of the list or None if there is no such node
        """

        # FIXME: Write this function

        cd_ll_iterator = self.head

        while cd_ll_iterator.next is not self.head:
            cd_ll_iterator = self.head.next
        return cd_ll_iterator


    def remove_front(self):
        """
        Removes the first element of the list. Will not remove the tail.
        """

        # FIXME: Write this function

        self.head.next.prev = self.head
        self.head = self.head.next


    def remove_back(self):
        """
        Removes the last element of the list. Will not remove the head.
        """

        # FIXME: Write this function

        cd_ll_iterator = self.head

        while cd_ll_iterator.next.next is not self.head:
            cd_ll_iterator = self.head.next
        self.head.prev = cd_ll_iterator
        cd_ll_iterator.next = self.head



    def is_empty(self):
        """
        Checks if the list is empty

        Returns:
            True if the list has no data nodes, False otherwise
        """

        # FIXME: Write this function

        if self.head.data is None and self.head.next is None:
            return True
        return False


    def contains(self, value):
        """
        Checks if any node contains value

        Args:
            value: The value to look for

        Returns:
            True if value is in the list, False otherwise
        """

        # FIXME: Write this function

        data_found = False
        for node in self.head:
            if value == node.data:
                data_found = True
            self.head = self.head.next
        return data_found

    def remove(self, value):
        """
        Removes the first instance of an element from the list

        Args:
            value: the value to remove
        """

        # FIXME: Write this function

        """cd_ll_iterator = self.head
        
        for node in self.head:
            if value == node.data:
                self.head = self.head.next.next
                
                return None
            cd_ll_iterator = self.head.next"""

        for node in self.head:
            if value == node.data:
                self.head.next.next.prev = self.head
                self.head.next = self.head.next.next
                return None
            self.head = self.head.next

    def circularListReverse(self):
        """
        Reverses the order of the links. It must not create any additional new links to do so.
        (e.g. you cannot call DLNode()). If the list printed by following next was 0, 1, 2, 3,
        after the call it will be 3,2,1,0
        """

        # FIXME: Write this function

        current_ptr = self.head
        #previous_pp
        while current_ptr is not self.head:
            current_ptr = self.head.next
            self.head.next = previous_ptr
            previous_ptr = self.head
            self.head = current_ptr

        """current_ptr = self.head
               # previous_pp
               while current_ptr is not self.head:
                   current_ptr = self.head.next
                   self.head.next = previous_ptr
                   previous_ptr = self.head
                   self.head = current_ptr"""

        """if self.sentinel.next is self.sentinel:
            return

        curr_ptr, prev_ptr = self.sentinel.next
        while curr_ptr is not self.sentinel:
            next_ptr = curr_ptr.next
            curr_ptr.next = prev_ptr
            prev_ptr = curr_ptr
            curr_ptr = next_ptr"""

        """if self.sentinel.prev is self.sentinel:
                    return 

                curr_ptr = self.sentinel.prev
                prev_ptr = curr_ptr

                while curr_ptr.prev is not self.sentinel:
                    curr_ptr = curr_ptr.prev
                    curr_ptr.prev = prev_ptr
                    prev_ptr = curr_ptr"""

    """if self.sentinel.next is self.sentinel:
         return

     curr_ptr = self.sentinel.next
     prev_ptr = self.sentinel.next
     while curr_ptr is not self.sentinel:
         next_ptr = curr_ptr.next
         curr_ptr.next = prev_ptr
         prev_ptr = curr_ptr
         curr_ptr = next_ptr"""
    """self.sentinel.next, self.sentinel.prev = self.sentinel.prev, self.sentinel.next

    curr_ptr = self.sentinel

    while self.sentinel.next is not self.sentinel:
        curr_ptr.next, curr_ptr.prev = curr_ptr.prev, curr_ptr.next
        curr_ptr = curr_ptr.next"""

    """"prev_ptr = self.sentinel
    curr_ptr = self.sentinel.next
    iter_ptr = self.sentinel.next
    next_ptr = self.sentinel.next.next

    while iter_ptr.next is not self.sentinel:
        curr_ptr.next = prev_ptr
        curr_ptr.prev = next_ptr
        iter_ptr = iter_ptr.next
    self.sentinel.next, self.sentinel.prev = self.sentinel.prev, self.sentinel.next"""

    # self.sentinel.prev, self.sentinel.next = self.sentinel.next, self.sentinel.prev
    # self.sentinel.

    # self.sentinel.next, self.sentinel.prev = self.sentinel.prev, self.sentinel.next

    # curr_ptr = self.sentinel
    # curr_ptr.prev = self.sentinel

    """if curr_ptr is not None:
        curr_ptr.next, curr_ptr.prev = curr_ptr.prev. curr_ptr.next
        curr_ptr = curr_ptr.prev
    while curr_ptr is not self.sentinel:
        curr_ptr.next, curr_ptr.prev = curr_ptr.prev.curr_ptr.next
        curr_ptr = curr_ptr.prev"""

    """while curr_ptr.next is not self.sentinel:
        next_ptr = curr_ptr.next
        prev_ptr = curr_ptr.prev
        curr_ptr.next = prev_ptr
        curr_ptr.prev = next_ptr
        curr_ptr = curr_ptr.next
    self.sentinel.prev = self.sentinel.next
    #self.sentinel.next, self.sentinel.prev = self.sentinel.prev, self.sentinel.next"""

    """while curr_ptr.prev is not self.sentinel:
        next_ptr = curr_ptr.prev
        prev_ptr = curr_ptr.next
        curr_ptr.next = prev_ptr
        curr_ptr.prev = next_ptr"""

    """#first_ptr = self.sentinel.next
           curr_ptr = self.sentinel.next
           #last_ptr = self.sentinel.prev
           #curr_ptr = curr_ptr.next.next
           while curr_ptr is not self.sentinel:
               #temp_ptr = curr_ptr.next
               #curr_ptr.next = curr_ptr.prev
               #curr_ptr.prev = temp_ptr
               curr_ptr.next, curr_ptr.prev = curr_ptr.prev, curr_ptr.next
               curr_ptr = curr_ptr.next
           self.sentinel.next, self.sentinel.prev = self.sentinel.prev, self.sentinel.next
           #self.sentinel.next = curr_ptr
           """

    """if self.sentinel.next is self.sentinel:
        return

    curr = self.sentinel
    last_node = self.sentinel.prev
    prev = None

    while curr is not last_node:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    self.sentinel.next = curr"""

