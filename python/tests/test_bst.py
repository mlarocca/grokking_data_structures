import unittest
from trees.bst import BinarySearchTree

class TestBinarySearchTree(unittest.TestCase):

    def test_repr(self):
        bst = BinarySearchTree()
        self.assertEqual(repr(bst), 'BinarySearchTree()')

        bst.insert(1)
        self.assertEqual(repr(bst), 'BinarySearchTree(1 ()())')

        bst.insert(2)
        bst.insert(-3.14)
        self.assertEqual(repr(bst), 'BinarySearchTree(1 (-3.14 ()())(2 ()()))')


    def test_str(self):
        bst = BinarySearchTree()
        self.assertEqual(str(bst), '')

        bst.insert('a')
        self.assertEqual(str(bst), 'a ()()')

        bst.insert('b')
        bst.insert('d')
        self.assertEqual(str(bst), 'a ()(b ()(d ()()))')
        bst.insert('c')
        self.assertEqual(str(bst), 'a ()(b ()(d (c ()())()))')
        bst.insert('Z')
        self.assertEqual(str(bst), 'a (Z ()())(b ()(d (c ()())()))')

    def test_len(self):
        bst = BinarySearchTree()
        self.assertEqual(len(bst), 0)

        bst.insert('a')
        self.assertEqual(len(bst), 1)

        bst.insert('b')
        bst.insert('d')
        self.assertEqual(len(bst), 3)
        bst.insert('c')
        self.assertEqual(len(bst), 4)
        bst.insert('Z')
        self.assertEqual(len(bst), 5)

    def test_contains(self):
        bst = BinarySearchTree()
        self.assertFalse(bst.contains('a'))
        self.assertFalse(bst.contains('b'))
        self.assertFalse(bst.contains('c'))
        self.assertFalse(bst.contains('d'))
        self.assertFalse(bst.contains('Z'))

        bst.insert('a')
        self.assertTrue(bst.contains('a'))
        self.assertFalse(bst.contains('b'))
        self.assertFalse(bst.contains('c'))
        self.assertFalse(bst.contains('d'))
        self.assertFalse(bst.contains('Z'))

        bst.insert('b')
        bst.insert('d')
        self.assertTrue(bst.contains('a'))
        self.assertTrue(bst.contains('b'))
        self.assertFalse(bst.contains('c'))
        self.assertTrue(bst.contains('d'))        
        self.assertFalse(bst.contains('Z'))

        bst.insert('c')
        self.assertTrue(bst.contains('c'))
        bst.insert('Z')
        self.assertTrue(bst.contains('Z'))
        bst.insert('A')
        self.assertTrue(bst.contains('A'))

    def test_insert_delete(self):
        bst = BinarySearchTree()

        # Delete from an empty BST
        with self.assertRaises(ValueError):
            bst.delete(6)

        bst.insert(6)
        bst.insert(4)
        bst.insert(7)
        bst.insert(5)
        bst.insert(2)
        bst.insert(3)
        bst.insert(9)
        bst.insert(1)
        bst.insert(6)
        bst.insert(8)
        bst.insert(11)

        self.assertEqual(len(bst), 11)

        # Value to be deleted not found
        with self.assertRaises(ValueError):
            bst.delete(0)

        # Delete a node with no children
        self.assertTrue(bst.contains(1))
        self.assertTrue(bst.contains(8))
        bst.delete(1)
        bst.delete(8)
        self.assertEqual(len(bst), 9)
        self.assertFalse(bst.contains(1))
        self.assertTrue(bst.contains(2))
        self.assertTrue(bst.contains(3))
        self.assertTrue(bst.contains(4))
        self.assertTrue(bst.contains(5))
        self.assertTrue(bst.contains(6))
        self.assertTrue(bst.contains(7))
        self.assertFalse(bst.contains(8))
        self.assertTrue(bst.contains(9))
        self.assertFalse(bst.contains(10))
        self.assertTrue(bst.contains(11))

        # Delete a node with only a left child
        bst.delete(9)
        self.assertEqual(len(bst), 8)
        self.assertFalse(bst.contains(1))
        self.assertTrue(bst.contains(2))
        self.assertTrue(bst.contains(3))
        self.assertTrue(bst.contains(4))
        self.assertTrue(bst.contains(5))
        self.assertTrue(bst.contains(6))
        self.assertTrue(bst.contains(7))
        self.assertFalse(bst.contains(8))
        self.assertFalse(bst.contains(9))
        self.assertFalse(bst.contains(10))
        self.assertTrue(bst.contains(11))

        # Delete a node with only a right child
        bst.delete(2)
        self.assertEqual(len(bst), 7)
        self.assertFalse(bst.contains(1))
        self.assertFalse(bst.contains(2))
        self.assertTrue(bst.contains(3))
        self.assertTrue(bst.contains(4))
        self.assertTrue(bst.contains(5))
        self.assertTrue(bst.contains(6))
        self.assertTrue(bst.contains(7))
        self.assertFalse(bst.contains(8))
        self.assertFalse(bst.contains(9))
        self.assertFalse(bst.contains(10))
        self.assertTrue(bst.contains(11))

        # Delete a node with both children
        bst.delete(4)
        self.assertEqual(len(bst), 6)
        self.assertFalse(bst.contains(1))
        self.assertFalse(bst.contains(2))
        self.assertTrue(bst.contains(3))
        self.assertFalse(bst.contains(4))
        self.assertTrue(bst.contains(5))
        self.assertTrue(bst.contains(6))
        self.assertTrue(bst.contains(7))
        self.assertFalse(bst.contains(8))
        self.assertFalse(bst.contains(9))
        self.assertFalse(bst.contains(10))
        self.assertTrue(bst.contains(11))

        # Delete the root node
        bst.delete(6)
        self.assertEqual(len(bst), 5)
        self.assertFalse(bst.contains(1))
        self.assertFalse(bst.contains(2))
        self.assertTrue(bst.contains(3))
        self.assertFalse(bst.contains(4))
        self.assertTrue(bst.contains(5))
        # There are two occurrences of the value 6!
        self.assertTrue(bst.contains(6))
        self.assertTrue(bst.contains(7))
        self.assertFalse(bst.contains(8))
        self.assertFalse(bst.contains(9))
        self.assertFalse(bst.contains(10))
        self.assertTrue(bst.contains(11))

        # It must have replaced the old root with
        # the other occurrence of the same value
        self.assertEqual(bst._root._value, 6)

        bst.delete(6)
        self.assertEqual(len(bst), 4)
        self.assertFalse(bst.contains(1))
        self.assertFalse(bst.contains(2))
        self.assertTrue(bst.contains(3))
        self.assertFalse(bst.contains(4))
        self.assertTrue(bst.contains(5))
        self.assertFalse(bst.contains(6))
        self.assertTrue(bst.contains(7))
        self.assertFalse(bst.contains(8))
        self.assertFalse(bst.contains(9))
        self.assertFalse(bst.contains(10))
        self.assertTrue(bst.contains(11))

        self.assertEqual(bst._root._value, 5)
        bst.insert(1)
        bst.insert(2)
        bst.insert(6)
        self.assertEqual(len(bst), 7)
        self.assertTrue(bst.contains(1))
        self.assertTrue(bst.contains(2))
        self.assertTrue(bst.contains(3))
        self.assertFalse(bst.contains(4))
        self.assertTrue(bst.contains(5))
        self.assertTrue(bst.contains(6))
        self.assertTrue(bst.contains(7))
        self.assertFalse(bst.contains(8))
        self.assertFalse(bst.contains(9))
        self.assertFalse(bst.contains(10))
        self.assertTrue(bst.contains(11))

        # Delete a node with both children, with the successor of the node having a left subtree
        bst = BinarySearchTree()

        bst.insert('H')
        bst.insert('F')
        bst.insert('I')
        bst.insert('G')
        bst.insert('B')
        bst.insert('E')
        bst.insert('K')
        bst.insert('A')
        bst.insert('J')
        bst.insert('L')
        bst.insert('C')
        bst.insert('D')
        self.assertEqual(len(bst), 12)

        bst.delete('F')
        self.assertEqual(len(bst), 11)
        self.assertTrue(bst.contains('A'))
        self.assertTrue(bst.contains('B'))
        self.assertTrue(bst.contains('C'))
        self.assertTrue(bst.contains('D'))
        self.assertTrue(bst.contains('E'))
        self.assertFalse(bst.contains('F'))
        self.assertTrue(bst.contains('G'))
        self.assertTrue(bst.contains('H'))
        self.assertTrue(bst.contains('I'))
        self.assertTrue(bst.contains('J'))
        self.assertTrue(bst.contains('K'))
        self.assertTrue(bst.contains('L'))



    def test_iterate(self):
        bst = BinarySearchTree()

        self.assertEqual([v for v in bst], [])

        bst.insert(6)

        self.assertEqual([v for v in bst], [6])

        bst.insert(4)

        self.assertEqual([v for v in bst], [4, 6])

        bst.insert(7)
        bst.insert(5)
        bst.insert(2)
        bst.insert(3)
        bst.insert(9)
        bst.insert(1)
        bst.insert(6)
        bst.insert(8)
        bst.insert(11)

        self.assertEqual([v for v in bst], [1, 2, 3, 4, 5, 6, 6, 7, 8, 9, 11])
