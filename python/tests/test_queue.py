import unittest
from queues.queue import Queue
from queues.queue_linked_list import Queue as QueueWithLinkedList

class TestQueueTemplate():
    def new_queue(self): # pragma: no cover
        raise NotImplementedError()

    def test_init(self):
        queue = self.new_queue()
        self.assertEqual(len(queue), 0)

    def test_enqueue_dequeue(self):
        queue = self.new_queue()
        self.assertEqual(len(queue), 0)

        # Dequeue from empty queue
        with self.assertRaises(ValueError):
            queue.dequeue()

        queue.enqueue('A')
        self.assertEqual(len(queue), 1)
        self.assertEqual(queue.dequeue(), 'A')
        self.assertEqual(len(queue), 0)

        # Dequeue from empty queue
        with self.assertRaises(ValueError):
            queue.dequeue()

        queue.enqueue('A')
        queue.enqueue('BB')
        queue.enqueue('CCC')
        self.assertEqual(len(queue), 3)
        self.assertEqual(queue.dequeue(), 'A')
        queue.enqueue(4)
        self.assertEqual(queue.dequeue(), 'BB')
        self.assertEqual(queue.dequeue(), 'CCC')
        self.assertEqual(queue.dequeue(), 4)


    def test_len(self):
        queue = self.new_queue()
        self.assertEqual(len(queue), 0)

        queue.enqueue(1)
        self.assertEqual(len(queue), 1)

        queue.enqueue(2)
        self.assertEqual(len(queue), 2)

        queue.enqueue(2)
        self.assertEqual(len(queue), 3)


    def test_is_empty(self):
        queue = self.new_queue()

        # Check empty queue
        self.assertTrue(queue.is_empty())

        # Check non-empty queue
        queue.enqueue(1)
        self.assertFalse(queue.is_empty())


    def test_iter(self):
        queue = self.new_queue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.dequeue()
        queue.enqueue(4)
        queue.enqueue(5)
        queue.dequeue()
        queue.enqueue(6)

        iterated = [x for x in queue]
        self.assertEqual(iterated, [3, 4, 5, 6])
        self.assertTrue(queue.is_empty())


class TestQueue(TestQueueTemplate, unittest.TestCase):
    """Tests a circular queue implemented with static arrays."""
    def new_queue(self, size=10):
        return Queue(size)


    # Tests specific to the array implementation
    def test_init_with_invalid_size(self):
        # Negative
        with self.assertRaises(ValueError):
            Queue(-1)
        # Null
        with self.assertRaises(ValueError):
            Queue(0)
        # Just one element
        with self.assertRaises(ValueError):
            Queue(1)


    def test_init_with_valid_size(self):
        queue = self.new_queue(2)
        queue.enqueue(1)
        queue.enqueue(2)
        with self.assertRaises(ValueError):
            queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 1)
        queue.enqueue(3)
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        with self.assertRaises(ValueError):
            queue.dequeue()
        queue.enqueue(4)
        self.assertEqual(len(queue), 1)
        self.assertEqual(queue.dequeue(), 4)


    def test_enqueue_to_a_full_queue(self):
        queue = self.new_queue(4)

        queue.enqueue(1)
        queue.enqueue('a')
        queue.enqueue(3)
        queue.enqueue('d')
        self.assertEqual(len(queue), 4)

        with self.assertRaises(ValueError):
            queue.enqueue('one too many')


    def test_repr(self):
        queue = self.new_queue()
        self.assertEqual(repr(queue), 'Queue([])')

        queue.enqueue(1)
        self.assertEqual(repr(queue), 'Queue([1])')

        queue.enqueue(2)
        queue.enqueue(3.14)

        self.assertEqual(repr(queue), 'Queue([1, 2, 3.14])')


    def test_str(self):
        queue = self.new_queue(5)
        self.assertEqual(str(queue), '[]')

        queue.enqueue('a')
        self.assertEqual(str(queue), '[\'a\']')

        queue.enqueue('b')
        queue.enqueue('c')

        self.assertEqual(str(queue), '[\'a\', \'b\', \'c\']')

        queue.dequeue()
        queue.enqueue('d')
        queue.enqueue('e')
        queue.dequeue()
        queue.enqueue('f')

        self.assertEqual(str(queue), '[\'c\', \'d\', \'e\', \'f\']')


class TestQueueLinkedList(TestQueueTemplate, unittest.TestCase):
    """Runs the tests for a queue implemented with linked lists."""
    def new_queue(self):
        return QueueWithLinkedList()
    
    def test_repr(self):
        queue = self.new_queue()
        self.assertEqual(repr(queue), 'Queue()')

        queue.enqueue(1)
        self.assertEqual(repr(queue), 'Queue(1)')

        queue.enqueue(2)
        queue.enqueue(3.14)

        self.assertEqual(repr(queue), 'Queue(1<->2<->3.14)')


    def test_str(self):
        queue = self.new_queue()
        self.assertEqual(str(queue), '')

        queue.enqueue('a')
        self.assertEqual(str(queue), 'a')

        queue.enqueue('b')
        queue.enqueue('c')

        self.assertEqual(str(queue), 'a<->b<->c')
