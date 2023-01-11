import lab3
import unittest


class T0_tree__insert(unittest.TestCase):

    def test_balanced_binary_search_tree(self):
        print("\n")
        print("tree_insert_with_individual_check")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        #The following check is without using tree as an iterator (which uses inorder traversal)
        #So this function also does not check the implementation of the traversal function

        self.assertEqual(t.root.data, 4)
        self.assertEqual(t.root.left.data, 2)
        self.assertEqual(t.root.left.left.data, 1)
        self.assertEqual(t.root.left.right.data, 3)
        self.assertEqual(t.root.right.data, 6)
        self.assertEqual(t.root.right.left.data, 5)
        self.assertEqual(t.root.right.right.data, 7)

        print("\n")

    def test_insert_1(self):
        """Insert test added by me (#1): checks to see if inserting single element into tree works
        and if children and parent are None"""
        t = lab3.Tree()
        t.insert(4)
        self.assertEqual(t.root.data, 4)
        self.assertEqual(t.root.parent, None)
        self.assertEqual(t.root.left, None)
        self.assertEqual(t.root.right, None)


class T1_min_and_max(unittest.TestCase):

    def test_min_and_max(self):
        print("\n")
        print("Checkin the min and the max functions")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)

        minimum = t.min()
        self.assertEqual(minimum, 1)
        maximum = t.max()
        self.assertEqual(maximum, 7)

        print("\n")

    def test_min_1(self):
        """Min test case added by me (#2): checks if None is returned on an
        empty tree"""
        t = lab3.Tree()
        minimum = t.min()
        self.assertEqual(minimum, None)

    def test_max_2(self):
        """Max test case added by me (#3): checks if None is returned on an empty
        tree"""
        t = lab3.Tree()
        max = t.max()
        self.assertEqual(max, None)

class T2_Traversal(unittest.TestCase):

    def test_traversal(self):
        print("\n")
        print("Checking all the three traversals")
        t = lab3.Tree()

        t.insert(4)
        t.insert(2)
        t.insert(6)
        t.insert(1)
        t.insert(3)
        t.insert(5)
        t.insert(7)
        tree_iterator = [node for node in t]
        inorder = [node for node in t.inorder()]
        preorder = [node for node in t.preorder()]
        

        print("__iter__(): inorder traversal")
        self.assertEqual(tree_iterator, [1, 2, 3, 4, 5, 6, 7])
        print("inorder traversal")
        self.assertEqual(inorder, [1, 2, 3, 4, 5, 6, 7])
        print("preorder traversal")
        self.assertEqual(preorder, [4, 2, 1, 3, 6, 5, 7])
        print("\n")

    def test_traversal_1(self):
        """Traversal test added by me (#4): checks that postorder traversal works correctly"""
        t = lab3.Tree()

        t.insert(7)
        t.insert(4)
        t.insert(9)
        t.insert(2)
        t.insert(3)
        t.insert(5)
        tree_iterator = [node for node in t]
        postorder = [node for node in t.postorder()]
        self.assertEqual(tree_iterator, [2, 3, 4, 5, 7, 9])
        self.assertEqual(postorder, [3, 2, 5, 4, 9, 7])

class T3_successor(unittest.TestCase):

    def test_successor(self):
        print("\n")
        print("successor function")
        tree_success = lab3.Tree()
        tree_success.insert(8)
        tree_success.insert(3)
        tree_success.insert(10)
        tree_success.insert(1)
        tree_success.insert(6)
        tree_success.insert(4)
        tree_success.insert(7)
        tree_success.insert(14)
        tree_success.insert(13)

        easy_success = tree_success.find_successor(8).data
        medium_success = tree_success.find_successor(10).data
        tough_success = tree_success.find_successor(7).data

        self.assertEqual(easy_success, 10)
        self.assertEqual(medium_success, 13)
        self.assertEqual(tough_success, 8)

        print("\n")

    def test_successor_1(self):
        """Successor test added by me (#5): checks if function can successfully find the inorder successor
        of given node"""
        t = lab3.Tree()
        t.insert(7)
        t.insert(3)
        t.insert(4)

        test = t.find_successor(4).data
        self.assertEqual(test, 7)


    def test_successor_2(self):
        """Successor test added by me (#6): checks if KeyError is raised on an empty tree"""
        t = lab3.Tree()
        with self.assertRaises(KeyError):
            t.find_successor(7)

    def test_successor_3(self):
        """Successor test added by me (#7): check if KeyError is raised when trying to find successor
        of node that is not in tree"""
        t = lab3.Tree()
        t.insert(3)
        t.insert(8)
        t.insert(5)
        t.insert(2)
        with self.assertRaises(KeyError):
            t.find_successor(7)

    def test_successor_4(self):
        """Successor test added by me (#8): checks that function returns None when there is no successor
        for existing node"""
        t = lab3.Tree()
        t.insert(4)
        t.insert(5)
        t.insert(1)
        self.assertEqual(t.find_successor(5), None)

    def test_successor_5(self):
        """Successor test added by me (#9): checks that function returns successor correctly"""
        t = lab3.Tree()
        t.insert(2)
        t.insert(1)
        t.insert(4)
        t.insert(3)
        t.insert(5)
        self.assertEqual(t.find_successor(2).data, 3)


class T4_delete(unittest.TestCase):

    def test_delete(self):
        print("\n")
        print("delete function")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)

        l1 = [node for node in t]
        t.delete(7)
        l2 = [node for node in t]
        t.delete(6)
        l3 = [node for node in t]
        t.delete(8)
        l4 = [node for node in t]
        t.delete(10)
        l5 = [node for node in t]

        self.assertEqual(l1, [1, 3, 4, 6, 7, 8, 10, 13, 14])
        self.assertEqual(l2, [1, 3, 4, 6, 8, 10, 13, 14])
        self.assertEqual(l3, [1, 3, 4, 8, 10, 13, 14])
        self.assertEqual(l4, [1, 3, 4, 10, 13, 14])
        self.assertEqual(l5, [1, 3, 4, 13, 14])

        print("\n")

    def test_delete_1(self):
        """Delete test added by me (#8): checks that 3 is no longer in tree"""
        t = lab3.Tree()
        t.insert(5)
        t.insert(3)
        t.insert(4)
        t.delete(3)
        self.assertEqual(t.contains(3), False)

    def test_delete_2(self):
        """Delete test added by me (#9): checks if KeyError is raised on an empty tree"""
        t = lab3.Tree()
        with self.assertRaises(KeyError):
            t.delete(7)

    def test_delete_3(self):
        """Delete test added by me (#10): checks if KeyError is raised when trying to delete node
        the doesn't exist in tree"""
        t = lab3.Tree()
        t.insert(9)
        t.insert(8)
        t.insert(3)
        t.insert(2)
        with self.assertRaises(KeyError):
            t.delete(7)

class T5_contains(unittest.TestCase):

    def test_contains(self):
        print("\n")
        print("contains function")
        t = lab3.Tree()
        t.insert(8)
        t.insert(3)
        t.insert(10)
        t.insert(1)
        t.insert(6)
        t.insert(4)
        t.insert(7)
        t.insert(14)
        t.insert(13)
        self.assertEqual(t.contains(13), True)
        self.assertEqual(t.contains(15), False)
        print("\n")

    def test_contains_1(self):
        """Contains test added by me (#11): checks if returns None on an empty tree"""
        t = lab3.Tree()
        self.assertEqual(t.contains(1), False)

    def test_find_node_1(self):
        """find_node test added by me (#12): checks that function can properly return
        node with that data or returns None if not found"""
        t = lab3.Tree()
        t.insert(4)
        t.insert(3)
        t.insert(7)
        t.insert(10)
        self.assertEqual(t.contains(3), True)
        self.assertEqual(t.contains(2), False)


if __name__ == '__main__' :
    unittest.main()