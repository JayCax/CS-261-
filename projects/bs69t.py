# bst6999.py
# ===================================================
# Implement a binary search tree that can store any
# arbitrary object in the tree.
# ===================================================


class Student:
    def __init__(self, number, name):
        self.grade = number  # this will serve as the object's key
        self.name = name

    def __lt__(self, kq):
        # FIXME: Write this function

        return self.grade < kq.grade

    def __gt__(self, kq):
        # FIXME: Write this function

        return self.grade > kq.grade

    def __eq__(self, kq):
        # FIXME: Write this function

        return self.grade == kq.grade

    def __str__(self):
        if self.grade is not None:
            # FIXME: Write this function
            return self.grade, self.name


class TreeNode:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val  # when this is a primitive, this serves as the node's key


class BST:
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
        Creates and adds a new node to the BSTree.
        If the BSTree is empty, the new node should added as the root.

        Args:
            val: Item to be stored in the new node
        """
        # FIXME: Write this function

        if bst_node.val > val:
            if bst_node.left is None:
                bst_node.left = TreeNode(val)
            else:
                self.add_recursive(bst_node.left, val)
        else:
            if bst_node.right is None:
                bst_node.right = TreeNode(val)
            else:
                self.add_recursive(bst_node.right, val)
        return

    def add(self, val):
        if not self.root:
            self.root = TreeNode(val)
        else:
            self.add_recursive(self.root, val)

        """
        if not self.root:
            self.root = TreeNode(val)
        else:
            curr_ptr = self.root
            parent_ptr = None
            while curr_ptr:
                parent_ptr = curr_ptr
                if val < curr_ptr.val:
                    curr_ptr = curr_ptr.left
                else:
                    curr_ptr = curr_ptr.right
            if val < parent_ptr.val:
                parent_ptr.left = TreeNode(val)
            else:
                parent_ptr.right = TreeNode(val)"""

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
            A list of nodes in the specified ordering
        """
        # FIXME: Write this function

        if visited is None:
            # first call to the function -> create container to store list of visited nodes
            # and initiate recursive calls starting with the root node
            visited = []

            self.pre_order_traversal(self.root, visited)
        if cur_node is None:
            return visited

        visited.append(cur_node.val)
        self.pre_order_traversal(cur_node.left, visited)
        self.pre_order_traversal(cur_node.right, visited)
        return visited

    def post_order_traversal(self, cur_node=None, visited=None) -> []:
        """
        Perform post-order traversal of the tree and return a list of visited nodes

        Returns:
            A list of nodes in the specified ordering
        """
        # FIXME: Write this function

        if visited is None:
            # first call to the function -> create container to store list of visited nodes
            # and initiate recursive calls starting with the root node
            visited = []
            self.post_order_traversal(self.root, visited)
        if cur_node is None:
            return visited

        self.post_order_traversal(cur_node.left, visited)
        self.post_order_traversal(cur_node.right, visited)
        visited.append(cur_node.val)
        return visited

    def contains_recursive(self, bst_node, kq):
        """
        Searches BSTree to determine if the query key (kq) is in the BSTree.

        Args:
            kq: query key

        Returns:
            True if kq is in the tree, otherwise False
        """
        # FIXME: Write this function
        """        if not self.root:
            self.root = TreeNode(val)
        else:
            curr_ptr = self.root
            parent_ptr = None
            while curr_ptr:
                parent_ptr = curr_ptr
                if val < curr_ptr.val:
                    curr_ptr = curr_ptr.left
                else:
                    curr_ptr = curr_ptr.right
            if val < parent_ptr.val:
                parent_ptr.left = TreeNode(val)
            else:
                parent_ptr.right = TreeNode(val)"""

        if bst_node.val == kq:
            return True
        elif bst_node.val > kq:
            if bst_node.left is None:
                return False
            return self.contains_recursive(bst_node.left, kq)
        elif bst_node.val < kq:
            if bst_node.right is None:
                return False
            return self.contains_recursive(bst_node.right, kq)
        else:
            return False

        """curr_ptr = self.root
        if curr_ptr.val == kq:
            return True
        elif curr_ptr.val > kq:
            if curr_ptr.left is None:
                return False
            self.contains(curr_ptr.left, kq)
        elif curr_ptr.val < kq:
            if curr_ptr.right is None:
                return False
            self.contains(curr_ptr.right, kq)
        else:
            return False
            """

    def contains(self, kq):
        if self.root is None:
            return False
        return self.contains_recursive(self.root, kq)

    def left_child(self, node):
        """
        Returns the left-most child in a subtree.

        Args:
            node: the root node of the subtree

        Returns:
            The left-most node of the given subtree
        """
        # FIXME: Write this function

        if isinstance(node, BST):
            bst_ptr = node.root
        if isinstance(node, TreeNode):
            bst_ptr = node

        while bst_ptr.left is not None:
            bst_ptr = bst_ptr.left
        # self.root.left = TreeNode(node)
        return bst_ptr

    def remove_recursive(self, bst_node, kq):
        
        """Removes node with key k, if the node exists in the BSTree.

        Args:
            node: root of Binary Search Tree
            kq: key of node to remove

        Returns:
            True if k is in the tree and successfully removed, otherwise False
            :param bst_node:"""
        
        # FIXME: Write this function

        if bst_node.val > kq:
            if bst_node.left is None and bst_node.right is None:
                return False
            return self.remove_recursive(bst_node.left, kq)

        elif bst_node.val < kq:
            if bst_node.left is None and bst_node.right is None:
                return False
            return self.remove_recursive(bst_node.right, kq)

        else:
            #if bst_node.left is None and bst_node.right is None:
                #bst_node.val = None
            if not bst_node.right:
                bst_node.val = bst_node.left
                #return True
            elif not bst_node.left:
                bst_node.val = bst_node.right
                #return True
            else:
                #temp = self.left_child(bst_node.right)
                bst_node.val = self.left_child(bst_node.right)
                # self.remove(self.left_child(self.root.right), self.temp.val)
                self.remove_recursive(bst_node.right, temp.val)
            return True
        #return False

    def remove(self, kq):
        if self.root is None:
            return
        else:
            self.remove_recursive(self.root, kq)

    """    def remove_iter(self, kq):

        if not self.root:
            return False
        parent_ptr = None
        curr_ptr = self.root

        while curr_ptr.val:
            if curr_ptr.val == kq:
                break
            parent_ptr.val = curr_ptr

            if curr_ptr.val > kq:
                if curr_ptr.left is None:
                    return False
                curr_ptr = curr_ptr.left
            else:
                if curr_ptr.right is None:
                    return False
                curr_ptr = curr_ptr.right

        if not curr_ptr.left:
            if parent_ptr is None:
                curr_ptr.val = curr_ptr.right
            else:
                if curr_ptr.val < parent_ptr.val:
                    parent_ptr.left = curr_ptr.right
                else:
                    parent_ptr.right = curr_ptr.right
        
        elif not curr_ptr.right:
            if parent_ptr is None:
                curr_ptr.val = curr_ptr.left
            else:
                if 
            parent_ptr = curr_ptr.left

        else:
            temp = self.left_child(curr_ptr.right)
            parent_ptr = temp
            self.remove_iter(temp)
        return True"""

    """def remove_iter(self, kq):

        if not self.root:
            return False
        parent_ptr = None
        curr_ptr = self.root

        while curr_ptr.val:
            if curr_ptr.val == kq:
                break
            parent_ptr.val = curr_ptr

            if curr_ptr.val > kq:
                if curr_ptr.left is None:
                    return False
                curr_ptr = curr_ptr.left
            else:
                if curr_ptr.right is None:
                    return False
                curr_ptr = curr_ptr.right

        if not curr_ptr.left:
            parent_ptr = curr_ptr.right
        elif not curr_ptr.right:
            parent_ptr = curr_ptr.left

        else:
            temp = self.left_child(curr_ptr.right)
            parent_ptr = temp
            self.remove_iter(temp)
        return True"""

    def remove_iter(self, kq):

        if not self.root:
            return False
        parent_ptr = None
        curr_ptr = self.root

        while curr_ptr.val:
            if curr_ptr.val == kq:
                break
            parent_ptr = curr_ptr

            if curr_ptr.val > kq:
                if curr_ptr.left is None:
                    return False
                curr_ptr = curr_ptr.left
            else:
                if curr_ptr.right is None:
                    return False
                curr_ptr = curr_ptr.right

        if not curr_ptr.left:
            if parent_ptr is None:
                curr_ptr.val = curr_ptr.right
            else:
                if curr_ptr.val < parent_ptr.val:
                    parent_ptr.left = curr_ptr.right
                else:
                    parent_ptr.right = curr_ptr.right

        elif not curr_ptr.right:
            if parent_ptr is None:
                curr_ptr.val = curr_ptr.left
            else:
                if curr_ptr.val < parent_ptr.val:
                    parent_ptr.left = curr_ptr.left
                else:
                    parent_ptr.right = curr_ptr.left
            #parent_ptr = curr_ptr.left

        else:
            temp = self.left_child(curr_ptr.right)
            temp.left = curr_ptr.left
            temp.right = curr_ptr.right

            if temp.val < parent_ptr.val:
                parent_ptr.left = temp
            else:
                parent_ptr.right = temp
            self.remove_leftmost_child_in_right_subtree(temp.right)

        return True

    def remove_leftmost_child_in_right_subtree(self, BST_node):
        #parent_ptr = None
        node_ptr = BST_node

        while node_ptr.left.left is not None:
            #parent_ptr = node_ptr
            node_ptr = node_ptr.left

        node_ptr.left = None

        return


    def get_first(self):
        """
        Gets the val of the root node in the BSTree.

        Returns:
            val of the root node, return None if BSTree is empty
        """
        # FIXME: Write this function

        return self.root.val

    def remove_first(self):
        """
        Removes the val of the root node in the BSTree.

        Returns:
            True if the root was removed, otherwise False
        """
        # FIXME: Write this function

        if not self.root:
            return
        elif not self.root.left and not self.root.right:
            self.root = None
        elif not self.root.right:
            self.root = self.root.left
        elif not self.root.left:
            self.root = self.root.right
        else:
            temp = self.left_child(self.root.right)
            self.root.val = temp.val
            self.remove(self.root.right, temp.val)
