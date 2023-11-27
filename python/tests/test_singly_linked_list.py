import unittest
from linked_lists.singly_linked_list import SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase):

    def test_init(self):
        linked_list = SinglyLinkedList()
        self.assertIsNone(linked_list._head)


    def test_len(self):
        linked_list = SinglyLinkedList()
        self.assertEqual(len(linked_list), 0)

        linked_list.insert_in_front(1)
        self.assertEqual(len(linked_list), 1)

        linked_list.insert_in_front(2)
        self.assertEqual(len(linked_list), 2)

        linked_list.insert_to_back(2)
        self.assertEqual(len(linked_list), 3)


    def test_repr(self):
        linked_list = SinglyLinkedList()
        self.assertEqual(repr(linked_list), 'SinglyLinkedList()')

        linked_list.insert_in_front(1)
        self.assertEqual(repr(linked_list), 'SinglyLinkedList(1)')

        linked_list.insert_in_front(2)
        self.assertEqual(repr(linked_list), 'SinglyLinkedList(2->1)')

        linked_list.insert_to_back(3.14)
        self.assertEqual(repr(linked_list), 'SinglyLinkedList(2->1->3.14)')


    def test_str(self):
        linked_list = SinglyLinkedList()
        self.assertEqual(str(linked_list), '')

        linked_list.insert_in_front('a')
        self.assertEqual(str(linked_list), 'a')

        linked_list.insert_in_front('b')
        self.assertEqual(str(linked_list), 'b->a')

        linked_list.insert_to_back('c')
        self.assertEqual(str(linked_list), 'b->a->c')


    def test_iter(self):
        linked_list = SinglyLinkedList()

        # Iterate over empty list
        self.assertEqual(list(linked_list), [])

        # Iterate over non-empty list
        linked_list.insert_in_front(1)
        linked_list.insert_in_front(2)
        linked_list.insert_to_back(3.14)
        linked_list.insert_to_back("AC")

        expected = [2, 1, 3.14, "AC"]
        self.assertEqual(list(linked_list), expected)


    def test_size(self):
        linked_list = SinglyLinkedList()
        self.assertEqual(linked_list.size(), 0)

        linked_list.insert_in_front(1)
        self.assertEqual(linked_list.size(), 1)

        linked_list.insert_in_front(2)
        self.assertEqual(linked_list.size(), 2)


    def test_is_empty(self):
        linked_list = SinglyLinkedList()
        self.assertTrue(linked_list.is_empty())
        linked_list.insert_in_front(1)
        self.assertFalse(linked_list.is_empty())
        linked_list.insert_in_front(2)
        linked_list.insert_in_front(3)
        self.assertFalse(linked_list.is_empty())

        linked_list.delete(3)
        self.assertFalse(linked_list.is_empty())

        linked_list.delete(2)
        self.assertFalse(linked_list.is_empty())

        linked_list.delete(1)
        self.assertTrue(linked_list.is_empty())


    def test_add_in_front(self):
        linked_list = SinglyLinkedList()

        # Add to empty list
        linked_list.insert_in_front(1)
        self.assertEqual(linked_list._head.data(), 1)

        # Add to non-empty list
        linked_list.insert_in_front(2)
        self.assertEqual(linked_list._head.data(), 2)
        self.assertEqual(linked_list._head.next().data(), 1)


    def test_add_to_back(self):
        linked_list = SinglyLinkedList()

        # Add to empty list
        linked_list.insert_to_back(1)
        self.assertEqual(linked_list._head.data(), 1)

        # Add to non-empty list
        linked_list.insert_in_front(2)
        linked_list.insert_to_back(3)
        self.assertEqual(linked_list._head.data(), 2)
        self.assertEqual(linked_list._head.next().data(), 1)
        self.assertEqual(linked_list._head.next().next().data(), 3)
        self.assertIsNone(linked_list._head.next().next().next())


    def test_get_valid_index(self):
        linked_list = SinglyLinkedList()
        linked_list.insert_in_front(1)
        linked_list.insert_in_front(2)
        linked_list.insert_in_front(3)

        self.assertEqual(linked_list.get(0), 3)
        self.assertEqual(linked_list.get(1), 2)
        self.assertEqual(linked_list.get(2), 1)

    def test_get_invalid_index(self):
        linked_list = SinglyLinkedList()

        with self.assertRaises(IndexError):
            linked_list.get(-1)

        with self.assertRaises(IndexError):
            linked_list.get(0) # index out of bounds

    def test_get_returns_deep_copy(self):
        linked_list = SinglyLinkedList()
        linked_list.insert_in_front([['a', 'b'], 1, 2])

        retrieved = linked_list.get(0)
        retrieved.append(3)
        retrieved[0].append('c')
        self.assertEqual(linked_list.get(0), [['a', 'b'], 1, 2])


    def test_internal_search(self):
        linked_list = SinglyLinkedList()

        # Search empty list
        self.assertIsNone(linked_list._search(1))

        # Search when not found
        linked_list.insert_in_front(2)
        linked_list.insert_in_front(1)
        self.assertIsNone(linked_list._search(3))

        # Search when found
        linked_list.insert_in_front(3)
        found = linked_list._search(3)
        self.assertEqual(found.data(), 3)


        found = linked_list._search(2)
        self.assertEqual(found.data(), 2)


    def test_search_empty_list(self):
        linked_list = SinglyLinkedList()
        result = linked_list.search(lambda x: x == 1)
        self.assertIsNone(result)

    def test_search_not_found(self):
        linked_list = SinglyLinkedList()
        linked_list.insert_in_front(2)
        linked_list.insert_in_front(3)
        result = linked_list.search(lambda x: x == 1)
        self.assertIsNone(result)

    def test_search_found(self):
        linked_list = SinglyLinkedList()
        linked_list.insert_in_front(3)
        linked_list.insert_in_front(2)
        linked_list.insert_in_front(1)
        result = linked_list.search(lambda x: x == 1)
        self.assertEqual(result, 1)
        result = linked_list.search(lambda x: x == 2)
        self.assertEqual(result, 2)
        result = linked_list.search(lambda x: x == 3)
        self.assertEqual(result, 3)

    def test_search_multiple_matches(self):
        linked_list = SinglyLinkedList()
        linked_list.insert_in_front('AB')
        linked_list.insert_in_front('C')
        linked_list.insert_in_front('ABC')
        linked_list.insert_in_front('B')
        result = linked_list.search(lambda x: x[0] == 'A')
        self.assertEqual(result, 'ABC')

    def test_delete(self):
        linked_list = SinglyLinkedList()
        linked_list.insert_in_front(1)
        linked_list.insert_in_front(2)
        linked_list.insert_in_front(3)

        linked_list.delete(2)

        self.assertEqual(len(linked_list), 2)
        self.assertEqual(linked_list._head.data(), 3)
        self.assertEqual(linked_list._head.next().data(), 1)


    def test_delete_head(self):
        linked_list = SinglyLinkedList()
        linked_list.insert_in_front(1)
        linked_list.insert_in_front(2)
        linked_list.insert_in_front(3)

        linked_list.delete(3)
        self.assertEqual(len(linked_list), 2)
        self.assertEqual(linked_list._head.data(), 2)
        self.assertEqual(linked_list._head.next().data(), 1)

        linked_list.delete(2)
        self.assertEqual(len(linked_list), 1)
        self.assertEqual(linked_list._head.data(), 1)
        self.assertIsNone(linked_list._head.next())

        linked_list.delete(1)
        self.assertEqual(len(linked_list), 0)


    def test_delete_invalid(self):
        linked_list = SinglyLinkedList()
        linked_list.insert_in_front(3)
        linked_list.insert_in_front(2)
        linked_list.insert_in_front(1)

        with self.assertRaises(ValueError):
            linked_list.delete(4)


    def test_delete_from_front(self):
        linked_list = SinglyLinkedList()

        # Delete from empty list
        with self.assertRaises(ValueError):
            linked_list.delete_from_front()

        # Delete from list with one element
        linked_list.insert_in_front(1)
        self.assertEqual(linked_list.delete_from_front(), 1)
        self.assertTrue(linked_list.is_empty())

        # Delete from list with multiple elements
        linked_list.insert_in_front(2)
        linked_list.insert_in_front(1)
        self.assertEqual(linked_list.delete_from_front(), 1)
        self.assertEqual(len(linked_list), 1)
        self.assertEqual(linked_list._head.data(), 2)


class TestNode(unittest.TestCase):

    def test_init(self):
        data = 'test'
        node = SinglyLinkedList.Node(data)
        self.assertEqual(node.data(), data)
        self.assertIsNone(node.next())

    def test_str(self):
        data = 'test'
        node = SinglyLinkedList.Node(data)
        self.assertEqual(str(node), str(data))

    def test_repr(self):
        data = 'test'
        node = SinglyLinkedList.Node(data)
        self.assertEqual(repr(node), repr(data))

    def test_next(self):
        node1 = SinglyLinkedList.Node(1)
        node2 = SinglyLinkedList.Node(2, node1)
        self.assertEqual(node2.next(), node1)

    def test_append(self):
        node1 = SinglyLinkedList.Node(1)
        node2 = SinglyLinkedList.Node(2)
        node1.append(node2)
        self.assertEqual(node1.next(), node2)

        node1.append(None)
        self.assertIsNone(node1.next())

    def test_has_next(self):
        node = SinglyLinkedList.Node(1)
        self.assertFalse(node.has_next())

        new_node = SinglyLinkedList.Node(2, node)
        self.assertTrue(new_node.has_next())
