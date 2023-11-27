import unittest
from arrays.core import Array

class TestArray(unittest.TestCase):
    # __init__
    def test_init_valid(self):
        """Test initializing Array with valid arguments"""
        arr = Array(5)
        self.assertEqual(len(arr), 5)
        self.assertEqual(arr[0], 0)
        arr = Array(3, 'f')
        self.assertEqual(len(arr), 3)
        self.assertEqual(arr[0], 0.0)

    def test_init_invalid_size(self):
        """Test initializing Array with invalid size"""
        with self.assertRaises(ValueError):
            Array(-1)

    def test_init_invalid_typecode(self):
        """Test initializing Array with invalid typecode"""
        with self.assertRaises(ValueError):
            Array(5, 'x')

    # __get_item__
    def test_get_item_valid(self):
        """Test getting an item with a valid index"""
        arr = Array(5)
        self.assertEqual(arr[0], 0)
        self.assertEqual(arr[1], 0)
        self.assertEqual(arr[2], 0)
        self.assertEqual(arr[3], 0)
        self.assertEqual(arr[4], 0)

        arr = Array(3, 'd')
        self.assertEqual(arr[0], 0.0)
        self.assertEqual(arr[1], 0.0)
        self.assertEqual(arr[2], 0.0)


    def test_get_item_invalid(self):
        """Test getting an item with an invalid index"""
        arr = Array(5)
        with self.assertRaises(IndexError):
            arr[-1]
        with self.assertRaises(IndexError):
            arr[5]

    # __set_item__
    def test_set_item_valid(self):
        """Test setting an item with a valid index"""
        arr = Array(5)
        arr[0] = -1
        arr[1] = 3
        arr[2] = 33
        arr[3] = 42
        arr[4] = -1000
        self.assertEqual(arr[0], -1)
        self.assertEqual(arr[1], 3)
        self.assertEqual(arr[2], 33)
        self.assertEqual(arr[3], 42)
        self.assertEqual(arr[4], -1000)

    def test_set_item_invalid_value(self):
        """Test setting an element with an invalid value"""
        arr = Array(5)
        with self.assertRaises(Exception):
            arr[0] = 1.3
        with self.assertRaises(Exception):
            arr[1] = '1'

    def test_set_item_invalid_index(self):
        """Test setting an item with an invalid index"""
        arr = Array(5)
        with self.assertRaises(IndexError):
            arr[-1] = 1
        with self.assertRaises(IndexError):
            arr[5] = 1

    # __len__
    def test_len(self):
        """Test getting the length of the array"""
        arr = Array(5)
        self.assertEqual(len(arr), 5)

        arr = Array(31, 'd')
        self.assertEqual(len(arr), 31)

    # __repr__
    def test_repr(self):
        """Test getting the string representation of the array"""
        arr = Array(5)
        arr[0] = 1
        arr[1] = 2
        arr[3] = -2
        self.assertEqual(repr(arr), "array('l', [1, 2, 0, -2, 0])")
