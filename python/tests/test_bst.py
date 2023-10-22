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
