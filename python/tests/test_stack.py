import unittest
from stacks.stack import Stack
from stacks.stack_dynamic_array import Stack as StackWithArray

class TestStackTemplate():
    def new_stack(self): # pragma: no cover
        raise NotImplementedError()

    def test_init(self):
        stack = self.new_stack()
        self.assertEqual(len(stack), 0)

    def test_push_pop(self):
        stack = self.new_stack()
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
        stack = self.new_stack()
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
        stack = self.new_stack()
        self.assertEqual(len(stack), 0)

        stack.push(1)
        self.assertEqual(len(stack), 1)

        stack.push(2)
        self.assertEqual(len(stack), 2)

        stack.push(2)
        self.assertEqual(len(stack), 3)


    def test_repr(self):
        stack = self.new_stack()
        self.assertEqual(repr(stack), 'Stack()')

        stack.push(1)
        self.assertEqual(repr(stack), 'Stack(1)')

        stack.push(2)
        stack.push(3.14)
        # When more than one element is in the stack, we can't put constraints on the order
        self.assertEqual(repr(stack), 'Stack(3.14->2->1)')


    def test_str(self):
        stack = self.new_stack()
        self.assertEqual(str(stack), '')

        stack.push('a')
        self.assertEqual(str(stack), 'a')

        stack.push('b')
        stack.push('c')
        # When more than one element is in the stack, we can't put constraints on the order
        self.assertEqual(str(stack), 'c->b->a')


    def test_is_empty(self):
        stack = self.new_stack()

        # Check empty stack
        self.assertTrue(stack.is_empty())

        # Check non-empty stack
        stack.push(1)
        self.assertFalse(stack.is_empty())


    def test_iter(self):
        stack = self.new_stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.pop()
        stack.push(4)
        stack.push(5)
        stack.pop()
        stack.push(6)

        iterated = [x for x in stack]
        self.assertEqual(iterated, [6, 4, 2, 1])
        self.assertTrue(stack.is_empty())


class TestStack(TestStackTemplate, unittest.TestCase):
    """Tests a stack implemented with linked lists."""
    def new_stack(self):
        return Stack()


class TestStackArray(TestStackTemplate, unittest.TestCase):
    """Runs the tests for a stack implemented with arrays (Python lists)."""
    def new_stack(self):
        return StackWithArray()

    # Additional tests specific to stack implemented with arrays
    def test_repr(self):
        stack = self.new_stack()
        self.assertEqual(repr(stack), 'Stack([])')

        stack.push(1)
        self.assertEqual(repr(stack), 'Stack([1])')

        stack.push(2)
        stack.push(3.14)
        self.assertEqual(repr(stack), 'Stack([3.14, 2, 1])')


    def test_str(self):
        stack = self.new_stack()
        self.assertEqual(str(stack), '[]')

        stack.push('a')
        self.assertEqual(str(stack), '[\'a\']')

        stack.push('b')
        stack.push('c')
        self.assertEqual(str(stack), '[\'c\', \'b\', \'a\']')
