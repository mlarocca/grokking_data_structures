import unittest
from arrays.sorted_array import SortedArray

class TestSortedArray(unittest.TestCase):
    # __init__

    def test_init(self):
        """Test initialization of SortedArray."""
        array = SortedArray(5)
        self.assertEqual(len(array), 0)

        array = SortedArray(3, 'f')
        self.assertEqual(len(array), 0)

    def test_init_invalid_size(self):
        """Test initializing Array with invalid size"""
        with self.assertRaises(ValueError):
            SortedArray(-1)

    def test_init_invalid_typecode(self):
        """Test initializing Array with invalid typecode"""
        with self.assertRaises(ValueError):
            SortedArray(5, 'x')


    # __len__

    def test_len(self):
        """Test length property."""
        array = SortedArray(5, 'i')
        self.assertEqual(len(array), 0)
        array.insert(1)
        self.assertEqual(len(array), 1)


    # __get_item__

    def test_getitem(self):
        """Test indexing into array."""
        array = SortedArray(5, 'i')
        array.insert(1)
        array.insert(2)
        self.assertEqual(array[0], 1)
        self.assertEqual(array[1], 2)

    def test_index_out_of_bounds(self):
        """Test that indexing past the end of the array raises an error."""
        array = SortedArray(5, 'i')
        array.insert(1)
        with self.assertRaises(IndexError):
            array[2]

    def test_negative_index(self):
        """Test that indexing with a negative index raises an error."""
        array = SortedArray(3, 'i')
        array.insert(431)
        with self.assertRaises(IndexError):
            array[-1]                    

    # __repr__

    def test_repr(self):
        """Test string representation."""
        array = SortedArray(5, 'i')
        array.insert(1)
        array.insert(2)
        self.assertEqual(repr(array), "SortedArray(array('i', [1, 2]))")


    # __iter__

    def test_iter(self):
        """Test iteration over values in the array."""
        array = SortedArray(8, 'i')
        array.insert(1)
        array.insert(2)
        array.insert(3)
        iterated_values = []
        for value in array:
            iterated_values.append(value)
        expected_values = [1, 2, 3]
        self.assertEqual(iterated_values, expected_values)

    def test_iter_empty(self):
        """Test that iteration over an empty array raises StopIteration."""
        array = SortedArray(3, 'i')
        with self.assertRaises(StopIteration):
            next(iter(array))


    # max_size

    def test_max_size(self):
        """Test the max_size method."""
        array = SortedArray(7, 'i')
        self.assertEqual(array.max_size(), 7)
        array.insert(1)
        self.assertEqual(array.max_size(), 7)
        array.insert(-2)
        self.assertEqual(array.max_size(), 7)       


    # insert

    def test_insert_full(self):
        """Test that insert raises an error if the array is full."""
        array = SortedArray(2, 'i')
        array.insert(1)
        array.insert(2)
        with self.assertRaises(ValueError):
            array.insert(3)

    def test_insert_sorted(self):
        """Test that insert places values in the correct sorted position."""
        array = SortedArray(6, 'i')
        array.insert(3)
        self.assertEqual(len(array), 1)        
        self.assertEqual(array[0], 3)
        array.insert(1)
        self.assertEqual(len(array), 2)        
        self.assertEqual(array[0], 1)
        self.assertEqual(array[1], 3)
        array.insert(2)
        self.assertEqual(len(array), 3)        
        self.assertEqual(array[0], 1)
        self.assertEqual(array[1], 2)
        self.assertEqual(array[2], 3)

    def test_insert_first(self):
        """Test that insert places the first value at index 0."""
        array = SortedArray(5, 'i')
        array.insert(1)
        self.assertEqual(array[0], 1)
        array.insert(-1)
        self.assertEqual(array[0], -1)
        self.assertEqual(len(array), 2)


    # search (linear)

    def test_linear_search_found(self):
        """Test searching for a value that is in the array."""
        array = SortedArray(4, 'i')
        array.insert(2)
        array.insert(1)
        array.insert(3)
        self.assertEqual(array.linear_search(2), 1)
        array.insert(-43)
        self.assertEqual(array.linear_search(-43), 0)
        array = SortedArray(3, 'd')
        array.insert(21.3)
        array.insert(3.1415)
        self.assertEqual(array.linear_search(3.1415), 0)

    def test_linear_search_not_found(self):
        """Test searching for a value that is not in the array."""
        array = SortedArray(5, 'i')
        array.insert(3)
        array.insert(1)
        array.insert(2)
        self.assertEqual(array.linear_search(4), None)

    def test_linear_search_empty(self):
        """Test searching an empty array."""
        array = SortedArray(2, 'i')
        self.assertEqual(array.linear_search(1), None)

    def test_linear_search_empty_chunk_not_included(self):
        """Test that only the filled portion of the array is searched."""
        array = SortedArray(5, 'i')
        array.insert(3)
        array.insert(1)
        array.insert(2)
        self.assertEqual(array.linear_search(0), None)
        array.insert(0)
        self.assertEqual(array.linear_search(0), 0)
        array = SortedArray(5, 'd')
        array.insert(-1.0)
        array.insert(-3)
        array.insert(-2)
        self.assertEqual(array.linear_search(0), None)
        self.assertEqual(array.linear_search(0.0), None)
        array.insert(0)
        self.assertEqual(array.linear_search(0), 3)


    # search (binary search)

    def test_find_found(self):
        """Test finding a value that is in the array."""
        array = SortedArray(7, 'i')
        array.insert(1)
        array.insert(3)
        array.insert(2)
        self.assertEqual(array.binary_search(2), 1)
        array.insert(-1)
        array.insert(23)
        array.insert(-2)
        self.assertEqual(array.binary_search(2), 3)
        self.assertEqual(array.binary_search(-1), 1)
        self.assertEqual(array.binary_search(-2), 0)
        self.assertEqual(array.binary_search(23), 5)

    def test_find_not_found(self):
        """Test finding a value that is not in the array."""
        array = SortedArray(5, 'i')
        array.insert(1)
        array.insert(2)
        array.insert(3)
        self.assertEqual(array.binary_search(4), None)
        self.assertEqual(array.binary_search(-10), None)

    def test_find_empty_chunk_not_included(self):
        """Test that only the filled portion of the array is searched."""
        array = SortedArray(5, 'i')
        array.insert(3)
        array.insert(1)
        array.insert(2)
        self.assertEqual(array.binary_search(0), None)
        array.insert(0)
        self.assertEqual(array.binary_search(0), 0)
        array = SortedArray(5, 'd')
        array.insert(-1.0)
        array.insert(-3)
        array.insert(-2)
        self.assertEqual(array.binary_search(0), None)
        self.assertEqual(array.binary_search(0.0), None)
        array.insert(0)
        self.assertEqual(array.binary_search(0), 3)        

    def test_find_empty(self):
        """Test finding a value in an empty array."""
        array = SortedArray(5, 'i')
        self.assertEqual(array.binary_search(1), None)
        self.assertEqual(array.binary_search(0), None)


    # delete

    def test_delete_found(self):
        """Test deleting a value that is in the array."""
        array = SortedArray(5, 'i')
        array.insert(1)
        array.insert(2)
        array.insert(3)
        self.assertEqual(len(array), 3)

        array.delete(2)
        self.assertEqual(len(array), 2)
        self.assertEqual(array[0], 1)
        self.assertEqual(array[1], 3)

        array = SortedArray(7, 'i')
        array.insert(3)
        array.insert(1)
        array.insert(3)
        array.insert(2)
        array.insert(2)
        self.assertEqual(len(array), 5)

        array.delete(2)
        self.assertEqual(len(array), 4)
        self.assertEqual(array[0], 1)
        self.assertEqual(array[1], 2)
        self.assertEqual(array[2], 3)
        self.assertEqual(array[3], 3)

        array.delete(3)
        self.assertEqual(len(array), 3)
        array.delete(1)
        self.assertEqual(len(array), 2)
        self.assertEqual(array[0], 2)
        self.assertEqual(array[1], 3)

        array.insert(0)
        array.insert(-3)
        array.insert(2)
        self.assertEqual(len(array), 5)

        array.delete(-3)
        self.assertEqual(len(array), 4)
        self.assertEqual(array[0], 0)
        self.assertEqual(array[1], 2)
        self.assertEqual(array[2], 2)
        self.assertEqual(array[3], 3)

        array.delete(2)
        self.assertEqual(len(array), 3)

        array.delete(2)
        array.delete(0)
        self.assertEqual(len(array), 1)
        self.assertEqual(array[0], 3)

        array.delete(3)
        self.assertEqual(len(array), 0)

    def test_delete_not_found(self):
        """Test deleting a value that is not in the array."""
        array = SortedArray(15, 'i')
        array.insert(1)
        array.insert(3)
        array.insert(2)
        with self.assertRaises(ValueError):
            array.delete(4)

    def test_delete_empty(self):
        """Test deleting from an empty array."""
        array = SortedArray(5, 'i')
        with self.assertRaises(ValueError):
            array.delete(1)
