import unittest
from linked_lists.singly_linked_list import SinglyLinkedList

class TestSinglyLinkedList(unittest.TestCase):

    def test_init(self):
        linked_list = SinglyLinkedList()
        self.assertIsNone(linked_list._head)


    def test_len(self):
        linked_list = SinglyLinkedList()
        self.assertEqual(len(linked_list), 0)

        linked_list.add_in_front(1)
        self.assertEqual(len(linked_list), 1)

        linked_list.add_in_front(2)
        self.assertEqual(len(linked_list), 2)

        linked_list.add_to_back(2)
        self.assertEqual(len(linked_list), 3)


    def test_repr(self):
        linked_list = SinglyLinkedList()
        self.assertEqual(repr(linked_list), '')

        linked_list.add_in_front(1)
        self.assertEqual(repr(linked_list), '1')

        linked_list.add_in_front(2)
        self.assertEqual(repr(linked_list), '2->1')

        linked_list.add_to_back(3.14)
        self.assertEqual(repr(linked_list), '2->1->3.14')


    def test_str(self):
        linked_list = SinglyLinkedList()
        self.assertEqual(str(linked_list), '')

        linked_list.add_in_front('a')
        self.assertEqual(str(linked_list), 'a')

        linked_list.add_in_front('b')
        self.assertEqual(str(linked_list), 'b->a')

        linked_list.add_to_back('c')
        self.assertEqual(str(linked_list), 'b->a->c')


    def test_size(self):
        linked_list = SinglyLinkedList()
        self.assertEqual(linked_list.size(), 0)

        linked_list.add_in_front(1)
        self.assertEqual(linked_list.size(), 1)

        linked_list.add_in_front(2)
        self.assertEqual(linked_list.size(), 2)


    def test_add_in_front(self):
        linked_list = SinglyLinkedList()

        # Add to empty list
        linked_list.add_in_front(1)
        self.assertEqual(linked_list._head.data(), 1)

        # Add to non-empty list
        linked_list.add_in_front(2)
        self.assertEqual(linked_list._head.data(), 2)
        self.assertEqual(linked_list._head.next().data(), 1)


    def test_add_to_back(self):
        linked_list = SinglyLinkedList()

        # Add to empty list
        linked_list.add_to_back(1)
        self.assertEqual(linked_list._head.data(), 1)

        # Add to non-empty list
        linked_list.add_in_front(2)
        linked_list.add_to_back(3)
        self.assertEqual(linked_list._head.data(), 2)
        self.assertEqual(linked_list._head.next().data(), 1)
        self.assertEqual(linked_list._head.next().next().data(), 3)
        self.assertIsNone(linked_list._head.next().next().next())


    def test_search(self):
        linked_list = SinglyLinkedList()

        # Search empty list
        self.assertIsNone(linked_list.search(1))

        # Search when not found
        linked_list.add_in_front(2)
        linked_list.add_in_front(1)
        self.assertIsNone(linked_list.search(3))

        # Search when found
        linked_list.add_in_front(3)
        found = linked_list.search(3)
        self.assertEqual(found.data(), 3)


        found = linked_list.search(2)
        self.assertEqual(found.data(), 2)


    def test_delete(self):
        linked_list = SinglyLinkedList()
        linked_list.add_in_front(1)
        linked_list.add_in_front(2)
        linked_list.add_in_front(3)

        linked_list.delete(2)

        self.assertEqual(len(linked_list), 2)
        self.assertEqual(linked_list._head.data(), 3)
        self.assertEqual(linked_list._head.next().data(), 1)


    def test_delete_head(self):
        linked_list = SinglyLinkedList()
        linked_list.add_in_front(1)
        linked_list.add_in_front(2)
        linked_list.add_in_front(3)

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
        linked_list.add_in_front(3)
        linked_list.add_in_front(2)
        linked_list.add_in_front(1)

        with self.assertRaises(ValueError):
            linked_list.delete(4)


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
