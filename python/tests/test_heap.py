import unittest
import random

from queues.heap import Heap

class HeapTest(unittest.TestCase):
    def test_init(self):
        heap = Heap()
        self.assertEqual(0, len(heap))

        heap = Heap(elements=['A', 'B', 'C', 'D'])

        self.assertEqual(4, len(heap))
        self.assertTrue(heap._validate())

        heap = Heap(elements=['A', 'B', 'C', 'D'], element_priority=lambda x: -ord(x))

        self.assertEqual(4, len(heap))
        self.assertTrue(heap._validate())


    def test_heapify(self):
        size = 4 + random.randint(0, 20)
        elements = [chr(i) for i in range(ord('A'), ord('Z'))[:size]]
        heap = Heap(elements=elements)

        self.assertEqual(size, len(heap))
        self.assertTrue(heap._validate())


        heap = Heap(elements=['A', 'B', 'C', 'D'])

        self.assertEqual(4, len(heap))
        self.assertEqual('D', heap.peek())

        heap = Heap(elements=['A', 'B', 'C', 'D'], element_priority=lambda x: -ord(x))        

        self.assertEqual(4, len(heap))
        self.assertEqual('A', heap.peek())


    def test_heapify_duplicates(self):
        # An heap populated with pairs, where the second element in the pair is the priority
        heap = Heap(elements=['A', 'A', 'A', 'D', 'D'])

        self.assertEqual(5, len(heap))
        self.assertEqual('D', heap.top())
        self.assertEqual('D', heap.top())
        self.assertEqual('A', heap.top())
        self.assertEqual(2, len(heap))

        heap = Heap(elements=['A', 'A', 'A', 'A'])

        self.assertEqual(4, len(heap))
        self.assertEqual('A', heap.top())


    def test_insert_top(self):
        heap = Heap([3, 1, 4, 11, -1, 2, 10])
        self.assertEqual(7, len(heap))
        heap.insert(7)
        heap.insert(5)
        self.assertEqual(9, len(heap))
        self.assertTrue(heap._validate())
        heap.top()
        heap.top()
        heap.top()
        self.assertEqual(6, len(heap))
        self.assertTrue(heap._validate())

        # An heap populated with pairs, where the second element in the pair is the priority
        heap = Heap(None, element_priority=lambda x: x[1])

        self.assertTrue(heap.is_empty())

        heap.insert(('First', -1e14))

        self.assertEqual('First', heap.top()[0])
        self.assertTrue(heap.is_empty())

        heap.insert(("b", 0))
        heap.insert(("c", 0.99))
        heap.insert(("second", 1))
        heap.insert(("a", -11))

        self.assertEqual('second', heap.top()[0])
        self.assertEqual(3, len(heap))

        for i in range(0, 10):
            heap.insert((str(i), random.random()))

        while not heap.is_empty():
            self.assertTrue(heap._validate())
            heap.top()


    def test_top_empty(self):
        heap = Heap()

        with self.assertRaises(ValueError):
            heap.top()

        with self.assertRaises(ValueError):
            heap.peek()
