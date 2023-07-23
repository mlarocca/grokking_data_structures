import unittest
from linked_lists.sorted_singly_linked_list import SortedSinglyLinkedList

class TestSortedSinglyLinkedList(unittest.TestCase):

    def test_insert(self):
        sorted_list = SortedSinglyLinkedList()

        # Insert into empty list
        sorted_list.insert(6)
        self.assertEqual(sorted_list._head.data(), 6)

        # Insert at head
        sorted_list.insert(3) 
        self.assertEqual(sorted_list._head.data(), 3)

        # Insert in middle
        sorted_list.insert(5)
        self.assertEqual(sorted_list._head.next().data(), 5)
        sorted_list.insert(4)
        self.assertEqual(sorted_list._head.next().data(), 4)

        # Insert at tail
        self.assertEqual(sorted_list._head.next().next().next().data(), 6)
        sorted_list.insert(7)
        self.assertEqual(sorted_list._head.next().next().next().data(), 6)
        self.assertEqual(sorted_list._head.next().next().next().next().data(), 7)

    def test_insert_in_front(self):
        sorted_list = SortedSinglyLinkedList()
        with self.assertRaises(NotImplementedError):
            sorted_list.insert_in_front(10)


    def test_insert_to_back(self):
        sorted_list = SortedSinglyLinkedList()
        with self.assertRaises(NotImplementedError):
            sorted_list.insert_to_back(10)


    def test_search(self):
        linked_list = SortedSinglyLinkedList()

        # Search empty list
        self.assertIsNone(linked_list._search(1))

        # Search when not found
        linked_list.insert(2)
        linked_list.insert(1)
        self.assertIsNone(linked_list._search(3))

        # Search when found
        linked_list.insert(3)
        found = linked_list._search(3)
        self.assertEqual(found.data(), 3)


        found = linked_list._search(2)
        self.assertEqual(found.data(), 2)


    def test_delete(self):
        linked_list = SortedSinglyLinkedList()
        linked_list.insert(1)
        linked_list.insert(2)
        linked_list.insert(3)

        linked_list.delete(2)

        self.assertEqual(len(linked_list), 2)
        self.assertEqual(linked_list._head.data(), 1)
        self.assertEqual(linked_list._head.next().data(), 3)