# Name: John-Francis Caccamo
# Date: 5 / 21 / 20
# Description:
# ===================================================
# This is the bst.py file. It will Implement a
# binary search tree that can store any
# arbitrary object in the tree. It will have a Student class
# with overloaded magic functions that will perform logical operations
# on Student objects. It will have a BST Tree class that will create
# a Binary Search Tree from Tree Nodes based on their values. Within
# the BST class will be methods that will manipulate, add / remove nodes
# and output the tree, be it pre, post or in-order traversal.
# ===================================================


class Student:
    """
    The Student class will create student objects and have magic, overloaded
    logic operators that will perform equivalence operations on Student
    objects in order to build a BST of Student objects.
    """
    def __init__(self, number, name):
        self.grade = number  # this will serve as the object's key
        self.name = name

    def __lt__(self, kq):
        """
        __lt__ will return True if a Student object's grade is less than a query's grade.
        """

        return self.grade < kq.grade

    def __gt__(self, kq):
        """
        __gt__ will return True if a Student object's grade is more than a query's grade.
        """

        return self.grade > kq.grade

    def __eq__(self, kq):
        """
        __eq__ will return True if a Student object's grade is equal to a query's grade.
        """

        return self.grade == kq.grade

    def __str__(self):
        """
        __str__ will publish the str representation of a Student object's grade plus
        the Student's name.
        """

        return str(self.grade) + " " + str(self.name)


class TreeNode:
    """
    The TreeNode class will represent the nodes of the BST with left and
    right pointers initialized to None.
    """
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val  # when this is a primitive, this serves as the node's key


class BST:
    """
    The BST class will construct, manipulate, add, delete and return the
    pre, post and in-order traversals of the BST.
    """
    def __init__(self, start_tree=None) -> None:
        """ Initialize empty tree """
        self.root = None

        # populate tree with initial nodes (if provided)
        if start_tree is not None:
            for value in start_tree:
                self.add(value)

    def __str__(self):
        """
        Traverses the tree using "in-order" traversal
        and returns content of tree nodes as a text string
        """
        values = [str(_) for _ in self.in_order_traversal()]
        return "TREE in order { " + ", ".join(values) + " }"

    def add_recursive(self, bst_node, val):
        """
        The add_recursive helper function to the add
        function. Will call the recursive cases in order
        to find the appropriate insertion location for the
        new BST node value.
        """

        if bst_node.val > val:  # if the argument value is less than that of current node
            if bst_node.left is None:  # if we have reached a node with no left children
                bst_node.left = TreeNode(val)  # make the left child the argument value
                return
            else:
                self.add_recursive(bst_node.left, val)  # otherwise continue recursing through the tree
        else:
            if bst_node.right is None:  # if the argument value is more than that of current node
                bst_node.right = TreeNode(val)  # if we have reached a node with no right children
                return
            else:
                self.add_recursive(bst_node.right, val) # otherwise continue recursing through the tree

    def add(self, val):
        """Creates and adds a new node to the BSTree.
        If the BSTree is empty, the new node should added as the root.

        Args:
            val: Item to be stored in the new node. The function
            will find the appropriate location for the new node
            by comparing its value to the values of existing nodes
            in the BST and lastly, add the value to the tree as
            a new TreeNode object."""

        if not self.root:  # if root doesn't exist
            self.root = TreeNode(val)  # establish argument value as the root
        else:
            self.add_recursive(self.root, val)  # otherwise call the recursive function

    def in_order_traversal(self, cur_node=None, visited=None) -> []:
        """
        Perform in-order traversal of the tree and return a list of visited nodes
        """

        if visited is None:
            # first call to the function -> create container to store list of visited nodes
            # and initiate recursive calls starting with the root node
            visited = []
            self.in_order_traversal(self.root, visited)

        # not a first call to the function
        # base case - reached the end of current subtree -> backtrack
        if cur_node is None:
            return visited

        # recursive case -> sequence of steps for in-order traversal:
        # visit left subtree, store current node value, visit right subtree
        self.in_order_traversal(cur_node.left, visited)
        visited.append(cur_node.val)
        self.in_order_traversal(cur_node.right, visited)
        return visited

    def pre_order_traversal(self, cur_node=None, visited=None) -> []:
        """
        Perform pre-order traversal of the tree and return a list of visited nodes

        Returns:
            A list of nodes in the specified ordering, with the root's value being
            returned first. Nodes will be returned in the order they are came
            across.
        """

        if visited is None:
            visited = []  # container to store list of visited nodes
            self.pre_order_traversal(self.root, visited)  # recurse from the root

        if cur_node is None:  # if we have reached current end of subtree
            return visited

        # values will be appended as they are visited
        visited.append(cur_node.val)  # append the root node and so on
        self.pre_order_traversal(cur_node.left, visited)  # recurse in the left subtree, appending from left to right
        self.pre_order_traversal(cur_node.right, visited)  # recurse in right subtree, appending from left to right

        return visited

    def post_order_traversal(self, cur_node=None, visited=None) -> []:
        """
        Perform post-order traversal of the tree and return a list of visited nodes

        Returns:
            A list of nodes in the specified ordering, with the root's value being
            returned last. Values will be appended and returned as their respective
            subtree terminates.
        """

        if visited is None:
            visited = []  # container to store list of visited nodes
            self.post_order_traversal(self.root, visited)  # start the recursive calls beginning with the root

        if cur_node is None:  # if we have reached current end of subtree
            return visited

        self.post_order_traversal(cur_node.left, visited)  # visit all values in left subtree
        self.post_order_traversal(cur_node.right, visited)  # visit all values in right subtree
        visited.append(cur_node.val)  # once all of current subtree is visited, append the node's value to visited

        return visited

    def contains_recursive(self, bst_node, kq):
        """
        The contains_recursive method will start at the root of the
        BST and recurse through the tree in order to find a node's value
        matching a query in which case it will return True. If the path
        through the BST ends in a None value, in which case the query
        does not exist, the function will return False.
        """

        if bst_node.val == kq:  # base case if query value is found
            return True

        elif bst_node.val > kq:  # if the query value is less than the current node's value
            if bst_node.left is None:  # if there is no path left
                return False
            return self.contains_recursive(bst_node.left, kq)  # recurse the function left one level down

        else:  # if the query value is greater than the current node's value
            if bst_node.right is None:  # if there is no path right
                return False
            return self.contains_recursive(bst_node.right, kq)  # recurse the function right one level down

    def contains(self, kq):
        """
        Searches BSTree to determine if the query key (kq) is in the BSTree.
        Contains will call the recursive method contains_recursive directly
        on the root via passing the self.root directly as its argument.

        Args:
            kq: query key

        Returns:
            True if kq is in the tree, otherwise False
        """

        if self.root is None:  # if there is no root to the BST
            return False

        return self.contains_recursive(self.root, kq)  # call the recursive function

    def left_child(self, node):
        """
        Returns the left-most child in a subtree. The method
        will check the instance of the argument, assign a
        pointer and iterate through the left children
        until left is not None.

        Args:
            node: the root node of the subtree

        Returns:
            The left-most node of the given subtree
        """

        if isinstance(node, BST):  # if node is of type BST
            bst_ptr = node.root  # assign bst_ptr to the root
        if isinstance(node, TreeNode):  # if node is of type TreeNode and an internal node
            bst_ptr = node  # assign bst_ptr to this node

        while bst_ptr.left is not None:  # iterate until the leftmost child is found
            bst_ptr = bst_ptr.left

        return bst_ptr  # return the leftmost child node

    def remove_recursive(self, bst_node, kq):
        """
        The remove_recursive helper function that will call recursion from the root
        of the BST down to its depth in order to find a removal query kq from which
        the first node matching this value will be deleted, replaced by its in-order
        successor. The bst_node argument will store the latest node of the recursive
        calls, starting from the root node.
        """

        if bst_node.val == kq:  # base case, the node to be deleted has been found

            if bst_node.right is None:  # no right subtree ->
                return bst_node.left  # replace with root of left subtree (including none)

            # at this point node has right subtree -> replace with leftmost child of right subtree
            left_child, parent_node = bst_node.right, bst_node  # make new pointers to right subtree and deletion node

            while left_child.left is not None:  # iterate until last left child node
                left_child, parent_node = left_child.left, left_child  # reassign the pointers
            bst_node.val = left_child.val  # reassign bst_node's value with the value of the leftmost child

            if parent_node is bst_node:  # the subsequent node from deletion has no left child
                parent_node.right = left_child.right  # assign bst_node's right value to left child's right
            else:
                parent_node.left = left_child.right  # make parent_node's left pointer to left child's right

            return bst_node  # return the BST with the appropriate removal

        if bst_node.val > kq:  # if the query value is less than the value of the current node
            bst_node.left = self.remove_recursive(bst_node.left, kq)  # recurse left down the BST 1 level
        else:   # if the query value is equal to or greater than the value of the current node
            bst_node.right = self.remove_recursive(bst_node.right, kq)  # recurse right down the BST 1 level

        return bst_node  # return the BST after recursion

    def remove(self, kq):
        """Removes node with key k, if the node exists in the BSTree. Remove will
        call the recursive steps on the BST root via passing the root directly
        as an argument to remove_recursive. If the
        root does not exist or if the value does not exist in the BST (via
        calling the contains function), remove will return False.
        Otherwise, the remove_function will call remove_recursive and the value
        will be removed.

        Args:
            node: root of Binary Search Tree
            kq: key of node to remove

        Returns:
            True if k is in the tree and successfully removed, otherwise False
        """

        if self.root is None:  # if there is no root in the BST
            return False
        else:
            if self.contains(kq):  # if the query value exists within the BST
                self.root = self.remove_recursive(self.root, kq)  # commence recursive calls starting at root
                return True  # return True if the value has been removed
            return False  # the query value does not exist in the BST

    def get_first(self):
        """
        Gets the val of the root node in the BSTree.

        Returns:
            val of the root node, return None if BSTree is empty
        """

        if self.root:  # if the root exists
            return self.root.val  # return the value held in the root

        return None  # if the root doesn't exist, return None 

    def remove_first(self):
        """
        Removes the val of the root node in the BSTree.
        If there is a right subtree, remove_first will
        call the remove method on the root
        to assign the new root value and delete leftmost child in right subtree.

        Additional decisions will occur based if there is only a left subtree
        or if the root has no children.

        Returns:
            True if the root was removed, otherwise False
        """

        if self.root:  # if root exits and tree is not empty

            if self.root.right:  # if there is a right subtree
                self.remove(self.root.val)  # call the remove method
            elif self.root.left:  # if no right subtree, simply reassign the root to self.root.left
                self.root = self.root.left
            else:  # if the root has no children
                self.root = None  # delete the root
            return True

        return False




