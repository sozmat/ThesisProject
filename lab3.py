class Node(object):
    def __init__(self, data):
        self.parent = None
        self.left = None
        self.right = None
        self.data = data


class Tree(object):
    """
    A class to represent a Binary Search Tree, BST

    Attributes:
    ----------
    root: None
        root of the tree


    Methods:
    --------
    insert(data):
        adds a node into the correct position for the BST
    __traverse(curr_node, traversal_type):
        generator function that goes through BST in either inorder, postorder,
        or preorder and gives the int values in specificied order
    __find_node(data):
        given an int, this function returns the node in the tree which holds
        data
    contains(data):
        given an int, this function returns True if there is some node in the tree
        containing data and False if there is not one
    find_successor(data):
        Find and return the node containing the next highest value from data.
    delete(data):
        Deletes the node associated with data from the tree.

    """
    # Binary Search Tree
    # class constants
    PREORDER = 1
    INORDER = 2
    POSTORDER = 3

    def __init__(self):
        # Do not create any other private variables.
        # You may create more helper methods as needed.
        self.root = None

    def print(self):
        # Print the data of all nodes in order
        self.__print(self.root)


    def __print(self, curr_node):
        # Recursively print a subtree (in order), rooted at curr_node
        if curr_node:
            self.__print(curr_node.left)
            print(str(curr_node.data), end=' ')  # save space
            self.__print(curr_node.right)
            

    def insert(self, data):
        """Inserts a node into BST which contains variable data"""
        # Find the right spot in the tree for the new node
        # Make sure to check if anything is in the tree
        # Hint: if a node n is None, calling n.data will cause an error
        d = Node(data)
        if self.root is None:
            self.root = d
        else:
            curr = self.root
            while curr is not None:
                if curr.data < d.data:
                    if curr.right is None:
                        d.parent = curr
                        curr.right = d
                        curr = None
                    else:
                        curr = curr.right
                else:       # if n is greater, go to right
                    if curr.data > d.data:
                        if curr.data > d.data:
                            if curr.left is None:
                                d.parent = curr
                                curr.left = d
                                curr = None
                            else:
                                curr = curr.left

    def min(self):
        """Returns the minimum value held in the tree and
        returns None if the tree is empty"""

        if self.root is None:
            return None
        else:
            curr = self.root
            while curr is not None:
                if curr.left is None:
                    return curr.data
                curr = curr.left
            return curr.data

    def max(self):
        """Returns the maximum value help in the tree and
        returns None if the tree is empty"""

        if self.root is None:
            return None
        else:
            curr = self.root
            while curr is not None:
                if curr.right is None:
                    return curr.data
                curr = curr.right
            return curr.data

    def __find_node(self, data):
        """Returns the node with that particular data value else returns None"""

        if self.root is None:   # if tree is empty then node definitely isn't in tree
            return None
        else:
            curr = self.root
            while curr is not None:
                if data > curr.data:
                    if curr.right is None:
                        break
                    else:
                        curr = curr.right
                elif data < curr.data:
                    if curr.left is None:
                        break
                    else:
                        curr = curr.left
                else:
                    if curr.data == data:
                        return curr


    def contains(self, data):
        """Returns True if node containing data is present in BST, else returns false"""
        x = self.__find_node(data)
        if x is None:
            return False
        else:
            return True

    def __iter__(self):
        """Iterate over the nodes with inorder traversal using a for loop"""
        return self.inorder()

    def inorder(self):
        """Inorder traversal : (LEFT, ROOT, RIGHT)"""
        return self.__traverse(self.root, Tree.INORDER)

    def preorder(self):
        """Preorder traversal : (ROOT, LEFT, RIGHT)"""
        return self.__traverse(self.root, Tree.PREORDER)

    def postorder(self):
        """Postorder traversal : (LEFT, RIGHT, ROOT)"""
        return self.__traverse(self.root, Tree.POSTORDER)

    def __traverse(self, curr_node, traversal_type):
        """Helper method using generators for traversals through BST, includes inorder, postorder, and preorder"""
        if traversal_type == Tree.INORDER:
            if curr_node:
                yield from self.__traverse(curr_node.left, traversal_type)
                yield curr_node.data
                yield from self.__traverse(curr_node.right, traversal_type)
        elif traversal_type == Tree.POSTORDER:
            if curr_node:
                yield from self.__traverse(curr_node.left, traversal_type)
                yield from self.__traverse(curr_node.right, traversal_type)
                yield curr_node.data
        else:
            # PREORDER
            if curr_node:
                yield curr_node.data
                yield from self.__traverse(curr_node.left, traversal_type)
                yield from self.__traverse(curr_node.right, traversal_type)


    def find_successor(self, data):
        """Returns the successor of the value passed through, data.
        If the value specified by find_successor does NOT exist in the tree, then raises a KeyError"""

        if not self.contains(data):     # node is not in tree, or tree is empty
            raise KeyError
        elif self.max() == data:        # node exists but has no successor
            return None
        else:
            # If the right subtree of the node is nonempty,then the successor is just
            # the leftmost node in the right subtree.
            curr = self.__find_node(data)  #  locating our node/ where it is in BST
            if curr.right is not None:
                # If right subtree is nonempty
                curr = curr.right
                while curr.left is not None:
                    if curr.left is None:
                        break
                    else:
                        curr = curr.left
            else:
                while curr.parent is not None:
                    if curr.parent is None:
                        break
                    else:
                        if curr == curr.left:
                            break
                        else:
                            curr = curr.parent
            return curr

    def delete(self, data):
        """Deletes a node of the BST, if node does not exist in tree then KeyError is raised. Tree rearranges as necessary
        according to how many children deleted node had"""

        if not self.contains(data):  # node is not in tree, or empty tree
            raise KeyError
        else:
            node = self.__find_node(data)
            #  a) The node has no children, just set its parent's pointer to None.
            if node.left is None and node.right is None:
                node_par = node.parent
                # figure out which child node was
                if node_par.left == node:
                    node_par.left = None
                else:
                    node_par.right = None
            elif node.left is not None and node.right is None:
                node_par = node.parent
                # node only has left child
                # set the parent pointer equal to node's child
                if node_par.left == node:
                    node_par.left = node.left
                else:
                    node_par.right = node.left
            elif node.left is None and node.right is not None:
                node_par = node.parent
                # node only has right child
                # set the parent pointer equal to node's child
                if node_par.left == node:
                    node_par.left = node.right
                else:
                    node_par.right = node.right
            else:
                # if two children, replace with successor and remove successor from position
                node_suc = self.find_successor(node.data)
                tmp = node_suc.data
                self.delete(node_suc.data)
                node.data = tmp

t = Tree()
t.insert(8)
t.insert(3)
t.insert(10)
t.insert(1)
t.insert(6)
t.insert(4)
t.insert(7)
t.insert(14)
t.insert(13)
t.print()
print("\n")
t.delete(7)
t.print()