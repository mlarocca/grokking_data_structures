import unittest
from stacks.stack import Stack

class TestStack(unittest.TestCase):

    def test_init(self):
        stack = Stack()
        self.assertEqual(len(stack), 0)

    def test_push_pop(self):
        stack = Stack()
        self.assertEqual(len(stack), 0)

        # Pop from empty stack
        with self.assertRaises(ValueError):
            stack.pop()

        stack.push('A')
        self.assertEqual(len(stack), 1)
        self.assertEqual(stack.pop(), 'A')
        self.assertEqual(len(stack), 0)

        # Pop from empty stack
        with self.assertRaises(ValueError):
            stack.pop()

        stack.push('A')
        stack.push('BB')
        stack.push('CCC')
        self.assertEqual(len(stack), 3)
        self.assertEqual(stack.pop(), 'CCC')
        stack.push(4)
        self.assertEqual(stack.pop(), 4)
        self.assertEqual(stack.pop(), 'BB')
        self.assertEqual(stack.pop(), 'A')


    def test_peek(self):
        stack = Stack()
        self.assertEqual(len(stack), 0)

        # Peek at empty stack
        with self.assertRaises(ValueError):
            stack.peek()

        stack.push('A')
        self.assertEqual(len(stack), 1)
        self.assertEqual(stack.peek(), 'A')
        self.assertEqual(len(stack), 1)

        stack.push('BB')
        stack.push('CCC')
        self.assertEqual(len(stack), 3)
        self.assertEqual(stack.peek(), 'CCC')
        self.assertEqual(stack.pop(), 'CCC')
        self.assertEqual(stack.peek(), 'BB')


    def test_len(self):
        stack = Stack()
        self.assertEqual(len(stack), 0)

        stack.push(1)
        self.assertEqual(len(stack), 1)

        stack.push(2)
        self.assertEqual(len(stack), 2)

        stack.push(2)
        self.assertEqual(len(stack), 3)


    def test_repr(self):
        stack = Stack()
        self.assertEqual(repr(stack), 'Stack()')

        stack.push(1)
        self.assertEqual(repr(stack), 'Stack(1)')

        stack.push(2)
        stack.push(3.14)
        # When more than one element is in the stack, we can't put constraints on the order
        self.assertEqual(repr(stack), 'Stack(3.14->2->1)')


    def test_str(self):
        stack = Stack()
        self.assertEqual(str(stack), '')

        stack.push('a')
        self.assertEqual(str(stack), 'a')

        stack.push('b')
        stack.push('c')
        # When more than one element is in the stack, we can't put constraints on the order
        self.assertEqual(str(stack), 'c->b->a')


    def test_is_empty(self):
        stack = Stack()

        # Check empty stack
        self.assertTrue(stack.is_empty())

        # Check non-empty stack
        stack.push(1)
        self.assertFalse(stack.is_empty())
