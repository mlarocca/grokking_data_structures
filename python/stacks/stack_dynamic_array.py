"""Module providing an implementation for stack, using singly-linked lists to store the elements."""

import copy
from typing import Any

class Stack:
    """ A class modeling the stack container.
    """
    def __init__(self) -> None:
        """ Creates an empty stack.
        """
        self._data = []


    def __len__(self):
        """
        Return the size of the stack.

        Parameters:
            None

        Returns:
            int: The number of values stored in the stack.
        """
        return len(self._data)


    def __iter__(self):
        """ Iterates on the elements of a stack.
            Warning: by doing so, the queue will be emptied.
        """
        while not self.is_empty():
            yield self.pop()


    def __str__(self):
        """
        Return the string representation of the stack.

        Parameters:
            None

        Returns:
            str: The string representation of the stack.
        """
        return str(self._data[::-1])


    def __repr__(self):
        """
        Return the string (internal) representation of the stack.

        Parameters:
            None

        Returns:
            str: The string representation of the stack.
        """
        return f'Stack({str(self._data[::-1])})'


    def is_empty(self) -> bool:
        """
        Check if the stack is empty.

        Parameters:
            None

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self._data) == 0


    def push(self, value: Any) -> None:
        """
        Add a new value to the stack.

        Parameters:
            value (Any): The value to insert into the stack.

        Returns:
            None
        """
        self._data.append(value)


    def pop(self) -> Any:
        """
        Remove and return the last value added to the stack.

        Parameters:
            None

        Returns:
            Any: The value removed from the stack.

        Raises:
            ValueError: If the stack is empty.
        """
        if self.is_empty():
            raise ValueError("Cannot pop from an empty stack")
        return self._data.pop()


    def peek(self) -> Any:
        """
        Return the last value added to the stack without removing it.

        Parameters:
            None

        Returns:
            Any: The value at the top of the stack.

        Raises:
            ValueError: If the stack is empty.
        """
        if self.is_empty():
            raise ValueError("Cannot peek at an empty stack")
        # We need to deepcopy the data from the list, otherwise
        # anyone with a reference can change the underlying data.
        return copy.deepcopy(self._data[-1])
