import unittest
from arrays.core import Array
from arrays.unsorted_array import insert_in_unsorted_array, delete_from_unsorted_array, find_in_unsorted_array, traverse_unsorted_array

class TestArray(unittest.TestCase):
    # __insert__

    def test_insert_valid(self):
        """Test inserting into an array with space"""
        arr = Array(5)
        current_size = insert_in_unsorted_array(1, arr, 0)
        self.assertEqual(current_size, 1)
        self.assertEqual(arr[0], 1)

    def test_insert_invalid(self):
        """Test inserting into a full array"""
        arr = Array(1)
        current_size = insert_in_unsorted_array(1, arr, 0)
        with self.assertRaises(ValueError):
            insert_in_unsorted_array(2, arr, 1)

    # delete

    def test_delete_valid(self):
        """Test deleting from an array with elements"""
        arr = Array(5)
        arr[0] = 1
        arr[1] = 2
        arr[2] = 3
        arr[3] = 4
        current_size = 4
        current_size = delete_from_unsorted_array(1, arr, current_size)
        self.assertEqual(current_size, 3)
        self.assertEqual(arr[1], 4)
        current_size = delete_from_unsorted_array(2, arr, current_size)
        self.assertEqual(current_size, 2)
        self.assertEqual(arr[0], 1)
        self.assertEqual(arr[1], 4)
        current_size = delete_from_unsorted_array(0, arr, current_size)
        self.assertEqual(current_size, 1)
        self.assertEqual(arr[0], 4)
        current_size = delete_from_unsorted_array(0, arr, current_size)
        self.assertEqual(current_size, 0)

    def test_delete_invalid_empty(self):
        """Test deleting from an empty array"""
        arr = Array(3)
        current_size = 0
        with self.assertRaises(ValueError):
            delete_from_unsorted_array(0, arr, current_size)

    def test_delete_invalid_index(self):
        """Test deleting with an invalid index"""
        arr = Array(5)
        arr[0] = 1
        current_size = 1
        with self.assertRaises(ValueError):
            delete_from_unsorted_array(1, arr, current_size)
        with self.assertRaises(ValueError):
            delete_from_unsorted_array(-1, arr, current_size)

    # find

    def test_find_in_unsorted_array_present(self):
        """Test finding an entry that is present in the array"""
        array = Array(7)
        array[0] = 4
        array[1] = -2
        array[2] = 55
        size = 3
        self.assertEqual(find_in_unsorted_array(-2, array, size), 1)
        self.assertEqual(find_in_unsorted_array(55, array, size), 2)
        self.assertEqual(find_in_unsorted_array(4, array, size), 0)

    def test_find_in_unsorted_array_absent(self):
        """Test finding an entry that is absent from the array"""
        array = Array(5)
        array[0] = 1
        array[1] = 2
        array[2] = 3
        size = 3
        index = find_in_unsorted_array(4, array, size)
        self.assertEqual(index, None)

    def test_find_in_unsorted_array_invalid_size(self):
        """Test finding an entry with an invalid size"""
        array = Array(5)
        array[0] = 1
        array[1] = 2
        array[2] = 3
        with self.assertRaises(ValueError):
            find_in_unsorted_array(2, array, size=6)

        with self.assertRaises(ValueError):
            find_in_unsorted_array(2, array, size=-1)

    # traverse

    def test_traverses_entire_array(self):
        result = []
        def test_callback(i: int):
            result.append(i + 1 )
        array = [1, 2, 3, 4, 5]
        traverse_unsorted_array(array, len(array), test_callback)
        self.assertEqual(result, [2, 3, 4, 5, 6])
