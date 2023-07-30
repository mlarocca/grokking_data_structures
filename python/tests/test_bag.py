import unittest
from bags.bag import Bag

class TestBag(unittest.TestCase):

    def test_init(self):
        bag = Bag()
        self.assertEqual(len(bag), 0)


    def test_len(self):
        bag = Bag()
        self.assertEqual(len(bag), 0)

        bag.insert(1)
        self.assertEqual(len(bag), 1)

        bag.insert(2)
        self.assertEqual(len(bag), 2)

        bag.insert(2)
        self.assertEqual(len(bag), 3)


    def test_repr(self):
        bag = Bag()
        self.assertEqual(repr(bag), 'Bag()')

        bag.insert(1)
        self.assertEqual(repr(bag), 'Bag(1)')

        bag.insert(2)
        bag.insert(3.14)
        # When more than one element is in the bag, we can't put constraints on the order
        self.assertTrue(repr(bag).startswith('Bag('))
        self.assertSetEqual(set(repr(bag).replace('Bag(', '').replace(')', '').split(',')), {'1', '2', '3.14'})


    def test_str(self):
        bag = Bag()
        self.assertEqual(str(bag), '')

        bag.insert('a')
        self.assertEqual(str(bag), 'a')

        bag.insert('b')
        bag.insert('c')
        # When more than one element is in the bag, we can't put constraints on the order
        self.assertEqual(set(str(bag).split(',')), {'c', 'b', 'a'})


    def test_iter(self):
        bag = Bag()

        # Iterate over empty list
        self.assertEqual(list(bag), [])

        # Iterate over non-empty list
        bag.insert(1)
        bag.insert(2)
        bag.insert(3.14)
        bag.insert("AC")

        expected = {1, 2, 3.14, "AC"}
        self.assertSetEqual(set(bag), expected)


    def test_is_empty(self):
        bag = Bag()

        # Check empty bag
        self.assertTrue(bag.is_empty())

        # Check non-empty bag
        bag.insert(1)
        self.assertFalse(bag.is_empty())
