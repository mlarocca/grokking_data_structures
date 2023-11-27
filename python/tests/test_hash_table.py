import unittest
from dictionaries.hash_table import HashTable

class TestHashTable(unittest.TestCase):

    def test_init_invalid_size(self):
        """Test initializing a HashTable with an invalid size"""
        with self.assertRaises(ValueError):
            HashTable(-1)

    def test_len(self):
        hash_table = HashTable(2)
        self.assertEqual(len(hash_table), 0)

        hash_table.insert('a')
        self.assertEqual(len(hash_table), 1)

        hash_table.insert('beta')
        hash_table.insert('delta')
        self.assertEqual(len(hash_table), 3)
        hash_table.insert('c')
        self.assertEqual(len(hash_table), 4)
        hash_table.insert('Jsut some random string')
        self.assertEqual(len(hash_table), 5)

    def test_is_empty(self):
        hash_table = HashTable(22)
        self.assertTrue(hash_table.is_empty())

        hash_table.insert('a')
        self.assertFalse(hash_table.is_empty())

        hash_table.insert('bba')
        self.assertFalse(hash_table.is_empty())

    def test_contains(self):
        hash_table = HashTable(3)
        self.assertFalse(hash_table.contains('a'))
        self.assertFalse(hash_table.contains('b'))
        self.assertFalse(hash_table.contains('c'))
        self.assertFalse(hash_table.contains('d'))
        self.assertFalse(hash_table.contains('Z'))

        hash_table.insert('a')
        self.assertTrue(hash_table.contains('a'))
        self.assertFalse(hash_table.contains('b'))
        self.assertFalse(hash_table.contains('c'))
        self.assertFalse(hash_table.contains('d'))
        self.assertFalse(hash_table.contains('Z'))

        hash_table.insert('b')
        hash_table.insert('d')
        self.assertTrue(hash_table.contains('a'))
        self.assertTrue(hash_table.contains('b'))
        self.assertFalse(hash_table.contains('c'))
        self.assertTrue(hash_table.contains('d'))        
        self.assertFalse(hash_table.contains('Z'))

        hash_table.insert('c')
        self.assertTrue(hash_table.contains('c'))
        hash_table.insert('Z')
        self.assertTrue(hash_table.contains('Z'))
        hash_table.insert('A')
        self.assertTrue(hash_table.contains('A'))

    def test_search(self):
        hash_table = HashTable(3)
        self.assertIsNone(hash_table.search(hash('a')))
        self.assertIsNone(hash_table.search(hash('b')))
        self.assertIsNone(hash_table.search(hash('c')))
        self.assertIsNone(hash_table.search(hash('d')))
        self.assertIsNone(hash_table.search(hash('Z')))

        hash_table.insert('a')
        self.assertEqual(hash_table.search(hash('a')), 'a')
        self.assertIsNone(hash_table.search(hash('b')))
        self.assertIsNone(hash_table.search(hash('c')))
        self.assertIsNone(hash_table.search(hash('d')))
        self.assertIsNone(hash_table.search(hash('Z')))

        hash_table.insert('b')
        hash_table.insert('d')
        self.assertEqual(hash_table.search(hash('a')), 'a')
        self.assertEqual(hash_table.search(hash('b')), 'b')
        self.assertIsNone(hash_table.search(hash('c')))
        self.assertEqual(hash_table.search(hash('d')), 'd')
        self.assertIsNone(hash_table.search(hash('Z')))

        hash_table.insert('c')
        self.assertEqual(hash_table.search(hash('c')), 'c')
        hash_table.insert('XYZ')
        self.assertEqual(hash_table.search(hash('XYZ')), 'XYZ')
        hash_table.insert(1)
        self.assertEqual(hash_table.search(hash(1)), 1)

        # Custom hash function
        key = lambda x: x * x * x
        hash_table = HashTable(5, extract_key=key)

        hash_table.insert(-1)
        hash_table.insert(0)
        hash_table.insert(1)
        hash_table.insert(2)
        self.assertEqual(hash_table.search(key(-1)), -1)
        self.assertEqual(hash_table.search(key(1)), 1)
        self.assertEqual(hash_table.search(key(0)), 0)
        self.assertEqual(hash_table.search(key(2)), 2)
        self.assertIsNone(hash_table.search(key(-2)))
        self.assertIsNone(hash_table.search(key(-3)))
        self.assertIsNone(hash_table.search(key(3)))
        self.assertIsNone(hash_table.search(key(0.4)))


    def test_insert_delete(self):
        hash_table = HashTable(5)

        # Delete from an empty hash_table
        with self.assertRaises(ValueError):
            hash_table.delete(6)

        hash_table.insert(6)
        hash_table.insert(4)
        hash_table.insert(7)
        hash_table.insert(5)
        hash_table.insert(2)
        hash_table.insert(3)
        hash_table.insert(9)
        hash_table.insert(1)
        hash_table.insert(6)
        hash_table.insert(8)
        hash_table.insert(11)

        self.assertEqual(len(hash_table), 11)

        # Value to be deleted not found
        with self.assertRaises(ValueError):
            hash_table.delete(0)

        self.assertTrue(hash_table.contains(1))
        self.assertTrue(hash_table.contains(8))
        hash_table.delete(1)
        hash_table.delete(8)
        self.assertEqual(len(hash_table), 9)
        self.assertFalse(hash_table.contains(1))
        self.assertTrue(hash_table.contains(2))
        self.assertTrue(hash_table.contains(3))
        self.assertTrue(hash_table.contains(4))
        self.assertTrue(hash_table.contains(5))
        self.assertTrue(hash_table.contains(6))
        self.assertTrue(hash_table.contains(7))
        self.assertFalse(hash_table.contains(8))
        self.assertTrue(hash_table.contains(9))
        self.assertFalse(hash_table.contains(10))
        self.assertTrue(hash_table.contains(11))

        hash_table.delete(9)
        self.assertEqual(len(hash_table), 8)
        self.assertFalse(hash_table.contains(1))
        self.assertTrue(hash_table.contains(2))
        self.assertTrue(hash_table.contains(3))
        self.assertTrue(hash_table.contains(4))
        self.assertTrue(hash_table.contains(5))
        self.assertTrue(hash_table.contains(6))
        self.assertTrue(hash_table.contains(7))
        self.assertFalse(hash_table.contains(8))
        self.assertFalse(hash_table.contains(9))
        self.assertFalse(hash_table.contains(10))
        self.assertTrue(hash_table.contains(11))

        hash_table.delete(2)
        self.assertEqual(len(hash_table), 7)
        self.assertFalse(hash_table.contains(1))
        self.assertFalse(hash_table.contains(2))
        self.assertTrue(hash_table.contains(3))
        self.assertTrue(hash_table.contains(4))
        self.assertTrue(hash_table.contains(5))
        self.assertTrue(hash_table.contains(6))
        self.assertTrue(hash_table.contains(7))
        self.assertFalse(hash_table.contains(8))
        self.assertFalse(hash_table.contains(9))
        self.assertFalse(hash_table.contains(10))
        self.assertTrue(hash_table.contains(11))

        hash_table.delete(4)
        self.assertEqual(len(hash_table), 6)
        self.assertFalse(hash_table.contains(1))
        self.assertFalse(hash_table.contains(2))
        self.assertTrue(hash_table.contains(3))
        self.assertFalse(hash_table.contains(4))
        self.assertTrue(hash_table.contains(5))
        self.assertTrue(hash_table.contains(6))
        self.assertTrue(hash_table.contains(7))
        self.assertFalse(hash_table.contains(8))
        self.assertFalse(hash_table.contains(9))
        self.assertFalse(hash_table.contains(10))
        self.assertTrue(hash_table.contains(11))

        hash_table.delete(6)
        self.assertEqual(len(hash_table), 5)
        self.assertFalse(hash_table.contains(1))
        self.assertFalse(hash_table.contains(2))
        self.assertTrue(hash_table.contains(3))
        self.assertFalse(hash_table.contains(4))
        self.assertTrue(hash_table.contains(5))

        # There are two occurrences of the value 6!
        self.assertTrue(hash_table.contains(6))
        self.assertTrue(hash_table.contains(7))
        self.assertFalse(hash_table.contains(8))
        self.assertFalse(hash_table.contains(9))
        self.assertFalse(hash_table.contains(10))
        self.assertTrue(hash_table.contains(11))

        hash_table.delete(6)
        self.assertEqual(len(hash_table), 4)
        self.assertFalse(hash_table.contains(1))
        self.assertFalse(hash_table.contains(2))
        self.assertTrue(hash_table.contains(3))
        self.assertFalse(hash_table.contains(4))
        self.assertTrue(hash_table.contains(5))
        self.assertFalse(hash_table.contains(6))
        self.assertTrue(hash_table.contains(7))
        self.assertFalse(hash_table.contains(8))
        self.assertFalse(hash_table.contains(9))
        self.assertFalse(hash_table.contains(10))
        self.assertTrue(hash_table.contains(11))

        hash_table.insert(1)
        hash_table.insert(2)
        hash_table.insert(6)
        self.assertEqual(len(hash_table), 7)
        self.assertTrue(hash_table.contains(1))
        self.assertTrue(hash_table.contains(2))
        self.assertTrue(hash_table.contains(3))
        self.assertFalse(hash_table.contains(4))
        self.assertTrue(hash_table.contains(5))
        self.assertTrue(hash_table.contains(6))
        self.assertTrue(hash_table.contains(7))
        self.assertFalse(hash_table.contains(8))
        self.assertFalse(hash_table.contains(9))
        self.assertFalse(hash_table.contains(10))
        self.assertTrue(hash_table.contains(11))
