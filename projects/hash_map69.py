# hash_map.py
# ===================================================
# Implement a hash map with chaining
# ===================================================

class SLNode:
    def __init__(self, key, value):
        self.next = None
        self.key = key
        self.value = value

    def __str__(self):
        return '(' + str(self.key) + ', ' + str(self.value) + ')'


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add_front(self, key, value):
        """Create a new node and inserts it at the front of the linked list
        Args:
            key: the key for the new node
            value: the value for the new node"""
        new_node = SLNode(key, value)
        new_node.next = self.head
        self.head = new_node
        self.size = self.size + 1

    def remove(self, key):
        """Removes node from linked list
        Args:
            key: key of the node to remove """
        if self.head is None:
            return False
        if self.head.key == key:
            self.head = self.head.next
            self.size = self.size - 1
            return True
        cur = self.head.next
        prev = self.head
        while cur is not None:
            if cur.key == key:
                prev.next = cur.next
                self.size = self.size - 1
                return True
            prev = cur
            cur = cur.next
        return False

    def contains(self, key):
        """Searches linked list for a node with a given key
        Args:
        	key: key of node
        Return:
        	node with matching key, otherwise None"""
        if self.head is not None:
            cur = self.head
            while cur is not None:
                if cur.key == key:
                    return cur
                cur = cur.next
        return None

    def __str__(self):
        out = '['
        if self.head != None:
            cur = self.head
            out = out + str(self.head)
            cur = cur.next
            while cur != None:
                out = out + ' -> ' + str(cur)
                cur = cur.next
        out = out + ']'
        return out


def hash_function_1(key):
    hash = 0
    for i in key:
        hash = hash + ord(i)
    return hash


def hash_function_2(key):
    hash = 0
    index = 0
    for i in key:
        hash = hash + (index + 1) * ord(i)
        index = index + 1
    return hash


class HashMap:
    """
    Creates a new hash map with the specified number of buckets.
    Args:
        capacity: the total number of buckets to be created in the hash table
        function: the hash function to use for hashing values
    """

    def __init__(self, capacity, function):
        self._buckets = []
        for i in range(capacity):
            self._buckets.append(LinkedList())
        self.capacity = capacity
        self._hash_function = function
        self.size = 0

    def return_buckets(self):
        return self._buckets

    def return_hash_function(self):
        return self._hash_function

    def call_hash_function(self, key):
        return self._hash_function(key) % self.capacity

    def clear(self):
        """
        Empties out the hash table deleting all links in the hash table.
        """
        # FIXME: Write this function

        for linked_list in self.return_buckets():
            if linked_list.head is not None:
                linked_list.head = None

        self.size = 0

    def get(self, key):
        """
        Returns the value with the given key.
        Args:
            key: the value of the key to look for
        Return:
            The value associated to the key. None if the link isn't found.
        """
        # FIXME: Write this function

        #return self.return_buckets()[self.call_hash_function(key)].head.next
        #return self.return_buckets()[key].head

        """values_of_ll = []
        if self.return_buckets()[self.call_hash_function(key)].head:
            while self.return_buckets()[self.call_hash_function(key)].head:
                values_of_ll.append(self.return_buckets()[self.call_hash_function(key)].head.next)
                self.return_buckets()[self.call_hash_function(key)].head.next = self.return_buckets()[self.call_hash_function(key)].head.next.next
                return values_of_ll
        return None"""

        if self.contains_key(key):
            ll_ptr = self.return_buckets()[self.call_hash_function(key)].head
            while ll_ptr is not None:

                if ll_ptr.key == key:
                    return ll_ptr.value
                ll_ptr = ll_ptr.next

        return None



    def resize_table(self, capacity):
        """
        Resizes the hash table to have a number of buckets equal to the given
        capacity. All links need to be rehashed in this function after resizing
        Args:
            capacity: the new number of buckets.
        """
        # FIXME: Write this function

        """new_hash_map = HashMap(capacity, self.return_hash_function())

        #count = 0
        for bucket in range(self.capacity()):
            new_hash_map.put(bucket, bucket.head)"""

        old_buckets = self._buckets
        old_size = self.size
        self._buckets = []
        self.capacity = capacity
        for i in range(capacity):
            self._buckets.append(LinkedList())


        """        for bucket in old_buckets:
            #for key, value in bucket:
            #print(bucket)
            if bucket.head:
                #for entry in bucket:
                ll_ptr = bucket.head
                while ll_ptr is not None:
                    self.put(ll_ptr.key, ll_ptr.value)
                    ll_ptr = ll_ptr.next"""

        for bucket in old_buckets:
            #for key, value in bucket:
            #print(bucket)
            if bucket.head:
                #for entry in bucket:
                ll_ptr = bucket.head
                while ll_ptr is not None:
                    self.put(ll_ptr.key, ll_ptr.value)
                    ll_ptr = ll_ptr.next
                    
        del old_buckets
        self.size = old_size

        return


    def put(self, key, value):
        """
        Updates the given key-value pair in the hash table. If a link with the given
        key already exists, this will just update the value and skip traversing. Otherwise,
        it will create a new link with the given key and value and add it to the table
        bucket's linked list.

        Args:
            key: they key to use to has the entry
            value: the value associated with the entry
        """
        # FIXME: Write this function

        #if not self.return_buckets()[self.call_hash_function(key)].next:
        #if not self.return_buckets()[self.call_hash_function(key)].head:
            #self.size += 1

        """if self.return_buckets()[self.call_hash_function(key)].head != key:
            self.size += 1
        self.return_buckets()[self.call_hash_function(key)].add_front(key, value)"""


        """if self.return_buckets()[self.call_hash_function(key)].head:
            self.return_buckets()[self.call_hash_function(key)].add_front(key, value)
        else:
            self.return_buckets()[self.call_hash_function(key)].head = SLNode(key, value)
        self.size += 1"""

        """if self.contains_key(key):
            key_in_ll = False
            ll_ptr = self.return_buckets()[self.call_hash_function(key)].head
            while ll_ptr is not None:

                if ll_ptr.key == key:
                    key_in_ll = True
                ll_ptr = ll_ptr.next
            if not key_in_ll:
                self.size += 1
            self.return_buckets()[self.call_hash_function(key)].add_front(key, value)
        else:
            self.return_buckets()[self.call_hash_function(key)].add_front(key, value)
            self.size += 1"""

        if self.contains_key(key):
            ll_ptr = self.return_buckets()[self.call_hash_function(key)]
            if ll_ptr.remove(key):
                self.size -= 1
        self.return_buckets()[self.call_hash_function(key)].add_front(key, value)
        self.size += 1
        return



    def remove(self, key):
        """
        Removes and frees the link with the given key from the table. If no such link
        exists, this does nothing. Remember to search the entire linked list at the
        bucket.
        Args:
            key: they key to search for and remove along with its value
        """
        # FIXME: Write this function

        #if self.return_buckets()[self.call_hash_function(key)].next:

        """if self.return_buckets()[self.call_hash_function(key)].next:
            ll_at_bucket = self.return_buckets()[self.call_hash_function(key)].next
            reduce_size = 0
            while ll_at_bucket:
                ll_at_bucket = ll_at_bucket.next
                reduce_size += 1
            self.size -= reduce_size"""

        """if self.return_buckets()[self.call_hash_function(key)]:
            self.size -= self.return_buckets()[self.call_hash_function(key)].size
            self.return_buckets()[self.call_hash_function(key)].next = None

        return"""

        if self.contains_key(key):
            #self.size -= self.return_buckets()[self.call_hash_function(key)].size
            #self.return_buckets()[self.call_hash_function(key)].next = None
            #cur_ptr = self.return_buckets()[self.call_hash_function(key)].head
            #prev_ptr = None

            #while ll_ptr is not None:
                #if ll_ptr.key == key:
            self.return_buckets()[self.call_hash_function(key)].remove(key)
            self.size -= 1

        return

    def contains_key(self, key):
        """
        Searches to see if a key exists within the hash table

        Returns:
            True if the key is found False otherwise

        """
        # FIXME: Write this function

        if self.return_buckets()[self.call_hash_function(key)].head:
            return True
        return False

    def empty_buckets(self):
        """
        Returns:
            The number of empty buckets in the table
        """
        # FIXME: Write this function

        #return self.capacity - self.size

        bucket_value = 0
        for bucket in self.return_buckets():
            if bucket.head:
                bucket_value += 1

        return self.capacity - bucket_value


    def table_load(self):
        """
        Returns:
            the ratio of (number of links) / (number of buckets) in the table as a float.

        """
        # FIXME: Write this function

        return self.size / self.capacity

    def __str__(self):
        """
        Prints all the links in each of the buckets in the table.
        """

        out = ""
        index = 0
        for bucket in self._buckets:
            out = out + str(index) + ': ' + str(bucket) + '\n'
            index = index + 1
        return out

"""student_map = HashMap(10, hash_function_1)
student_map_func2 = HashMap(10, hash_function_2)

first_node = ("test_val", 5)
collision_node = ("test_5", 5)

student_map.put(first_node[0], first_node[1])
student_map_func2.put(first_node[0], first_node[1])

student_map.put(first_node[0], -5)

student_map.put(collision_node[0], collision_node[1])

print(student_map)

print(student_map.size)"""

# resize


def get_keys_from_map(map):
    to_return = []
    for bucket in map._buckets:
        cur_node = bucket.head
        while cur_node is not None:
            to_return.append(cur_node.key)
            cur_node = cur_node.next
    return to_return

test_values = [("test_5", 5), ("test_-5", -5), ("test_5_", 5), ("diff_word", 15), ("another_word", 20),
                       ("set", 10), ("anotha_one", -7), ("completely_different", 5), ("getting_there", -1)]
student_map = HashMap(10, hash_function_1)
for key, value in test_values:
    student_map.put(key, value)

keys_before_resize = get_keys_from_map(student_map)
size_before_resize = student_map.size
print(student_map)

student_map.resize_table(50)
keys_after_resize = get_keys_from_map(student_map)
size_after_resize = student_map.size
print(student_map)
