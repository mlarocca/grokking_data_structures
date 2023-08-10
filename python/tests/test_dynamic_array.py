import unittest
from arrays.dynamic_array import DynamicArray

class TestDynamicArray(unittest.TestCase):
    # __init__
    
    def test_init(self):
        """Test initialization of DynamicArray."""
        array = DynamicArray(5)
        self.assertEqual(len(array), 0)

        array = DynamicArray(3, 'f')
        self.assertEqual(len(array), 0)

    def test_init_capacity(self):
        """Test that the right capacity is set on initialization of DynamicArray."""
        array = DynamicArray()
        self.assertEqual(len(array), 0)
        self.assertEqual(array._capacity, 1)

        array = DynamicArray(3, 'f')
        self.assertEqual(len(array), 0)
        self.assertEqual(array._capacity, 3)


    def test_init_invalid_size(self):
        """Test initializing Array with invalid size"""
        with self.assertRaises(ValueError):
            DynamicArray(-1)

    def test_init_invalid_typecode(self):
        """Test initializing Array with invalid typecode"""
        with self.assertRaises(ValueError):
            DynamicArray(5, 'x')


    # __len__

    def test_len(self):
        """Test length property."""
        array = DynamicArray(5, 'i')
        self.assertEqual(len(array), 0)
        array.insert(1)
        self.assertEqual(len(array), 1)


    # __get_item__

    def test_getitem(self):
        """Test indexing into array."""
        array = DynamicArray(5, 'i')
        array.insert(1)
        array.insert(2)
        self.assertEqual(array[0], 1)
        self.assertEqual(array[1], 2)

    def test_index_out_of_bounds(self):
        """Test that indexing past the end of the array raises an error."""
        array = DynamicArray(5, 'i')
        array.insert(1)
        with self.assertRaises(IndexError):
            array[2]

    def test_negative_index(self):
        """Test that indexing with a negative index raises an error."""
        array = DynamicArray(3, 'i')
        array.insert(431)
        with self.assertRaises(IndexError):
            array[-1]                    

    # __repr__

    def test_repr(self):
        """Test string representation."""
        array = DynamicArray(5, 'i')
        array.insert(1)
        array.insert(2)
        self.assertEqual(repr(array), "array('i', [1, 2])")


    # __iter__

    def test_iter(self):
        """Test iteration over values in the array."""
        array = DynamicArray(8, 'i')
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
        array = DynamicArray(3, 'i')
        with self.assertRaises(StopIteration):
            next(iter(array))


    # insert

    def test_insert_full(self):
        """Test that insert resizes the array correctly"""
        array = DynamicArray(typecode = 'i')
        array.insert(1)
        self.assertEqual(array._capacity, 1)
        array.insert(2)
        self.assertEqual(len(array), 2)
        self.assertEqual(array._capacity, 2)
        array.insert(3)
        self.assertEqual(3, len(array))
        self.assertEqual(array._capacity, 4)
        self.assertEqual([v for v in array], [1,2,3])

        array = DynamicArray(3, 'i')
        array.insert(1)
        self.assertEqual(array._capacity, 3)
        array.insert(2)
        self.assertEqual(len(array), 2)
        self.assertEqual(array._capacity, 3)
        array.insert(3)
        self.assertEqual(3, len(array))
        self.assertEqual(array._capacity, 3)
        array.insert(4)
        self.assertEqual(4, len(array))
        self.assertEqual(array._capacity, 6)
        self.assertEqual([v for v in array], [1,2,3,4])

    # search

    def test_find_found(self):
        """Test searching for a value that is in the array."""
        array = DynamicArray(4, 'i')
        array.insert(2)
        array.insert(1)
        array.insert(3)
        self.assertEqual(array.find(2), 0)
        array.insert(-43)
        self.assertEqual(array.find(-43), 3)
        array = DynamicArray(3, 'd')
        array.insert(21.3)
        array.insert(3.1415)
        self.assertEqual(array.find(3.1415), 1)

    def test_find_not_found(self):
        """Test searching for a value that is not in the array."""
        array = DynamicArray(5, 'i')
        array.insert(3)
        array.insert(1)
        array.insert(2)
        self.assertEqual(array.find(4), None)

    def test_find_empty(self):
        """Test searching an empty array."""
        array = DynamicArray(2, 'i')
        self.assertEqual(array.find(1), None)

    def test_find_empty_chunk_not_included(self):
        """Test that only the filled portion of the array is searched."""
        array = DynamicArray(5, 'i')
        array.insert(3)
        array.insert(1)
        array.insert(2)
        self.assertEqual(array.find(0), None)
        array.insert(0)
        self.assertEqual(array.find(0), 3)
        array = DynamicArray(5, 'd')
        array.insert(-1.0)
        array.insert(-3)
        array.insert(-2)
        self.assertEqual(array.find(0), None)
        self.assertEqual(array.find(0.0), None)
        array.insert(0)
        self.assertEqual(array.find(0), 3)
        self.assertEqual(array.find(-2), 2)
        self.assertEqual(array.find(-1), 0)
        array.delete(-2)
        self.assertEqual(array.find(-2), None)
        array.delete(-1)
        self.assertEqual(array.find(-1), None)

    # is_empty

    def test_is_empty(self):
        """Test the is_empty method."""
        array = DynamicArray(2, 'i')
        self.assertTrue(array.is_empty())
        array.insert(1)
        self.assertFalse(array.is_empty())
        array.insert(3)
        array.insert(2)
        self.assertFalse(array.is_empty())

    # delete

    def test_delete_found(self):
        """Test deleting a value that is in the array."""
        array = DynamicArray(5, 'i')
        array.insert(1)
        array.insert(2)
        array.insert(3)
        self.assertEqual(len(array), 3)

        array.delete(2)
        self.assertEqual(len(array), 2)
        self.assertEqual(array[0], 1)
        self.assertEqual(array[1], 3)

        array = DynamicArray(7, 'i')
        array.insert(3)
        array.insert(1)
        array.insert(3)
        array.insert(2)
        array.insert(2)
        self.assertEqual(len(array), 5)

        array.delete(2)
        self.assertEqual(len(array), 4)
        self.assertEqual(array[0], 3)
        self.assertEqual(array[1], 1)
        self.assertEqual(array[2], 3)
        self.assertEqual(array[3], 2)

        array.delete(3)
        self.assertEqual(len(array), 3)
        array.delete(1)
        self.assertEqual(len(array), 2)
        self.assertEqual(array[0], 3)
        self.assertEqual(array[1], 2)

        array.insert(0)
        array.insert(-3)
        array.insert(2)
        self.assertEqual(len(array), 5)

        array.delete(-3)
        self.assertEqual(len(array), 4)
        self.assertEqual(array[0], 3)
        self.assertEqual(array[1], 2)
        self.assertEqual(array[2], 0)
        self.assertEqual(array[3], 2)

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
        array = DynamicArray(15, 'i')
        array.insert(1)
        array.insert(3)
        array.insert(2)
        with self.assertRaises(ValueError):
            array.delete(4)

    def test_delete_empty(self):
        """Test deleting from an empty array."""
        array = DynamicArray(5, 'i')
        with self.assertRaises(ValueError):
            array.delete(1)

    # resize (internal)

    def test_resizing(self):
        array = DynamicArray()
        self.assertEqual(len(array), 0)
        self.assertEqual(array._capacity, 1)
        array.insert(1)
        self.assertEqual(len(array), 1)
        self.assertEqual(array._capacity, 1)
        array.insert(2)
        self.assertEqual(len(array), 2)
        self.assertEqual(array._capacity, 2)
        array.insert(3)
        self.assertEqual(len(array), 3)
        self.assertEqual(array._capacity, 4)

        array.delete(2)
        self.assertEqual(len(array), 2)
        self.assertEqual(array._capacity, 4)
        array.delete(1)
        self.assertEqual(len(array), 1)
        self.assertEqual(array._capacity, 2)

        # Initial capacity > 1
        array = DynamicArray(3, 'i')
        self.assertEqual(len(array), 0)
        self.assertEqual(array._capacity, 3)
        array.insert(3)
        self.assertEqual(len(array), 1)
        self.assertEqual(array._capacity, 3)
        array.insert(1)
        self.assertEqual(len(array), 2)
        self.assertEqual(array._capacity, 3)
        array.insert(3)
        self.assertEqual(len(array), 3)
        self.assertEqual(array._capacity, 3)
        array.insert(2)
        self.assertEqual(len(array), 4)
        self.assertEqual(array._capacity, 6)
        array.insert(2)
        self.assertEqual(len(array), 5)
        self.assertEqual(array._capacity, 6)
        array.insert(21)
        self.assertEqual(len(array), 6)
        self.assertEqual(array._capacity, 6)
        array.insert(-31)
        self.assertEqual(len(array), 7)
        self.assertEqual(array._capacity, 12)

        array.delete(2)
        self.assertEqual(len(array), 6)
        self.assertEqual(array._capacity, 12)
        array.delete(21)
        self.assertEqual(len(array), 5)
        self.assertEqual(array._capacity, 12)
        array.delete(2)
        self.assertEqual(len(array), 4)
        self.assertEqual(array._capacity, 12)
        array.delete(3)
        self.assertEqual(len(array), 3)
        self.assertEqual(array._capacity, 6)
        array.delete(1)
        self.assertEqual(len(array), 2)
        self.assertEqual(array._capacity, 6)
        array.delete(-31)
        self.assertEqual(len(array), 1)
        self.assertEqual(array._capacity, 3)
        array.delete(3)
        self.assertEqual(len(array), 0)
        self.assertEqual(array._capacity, 1)
