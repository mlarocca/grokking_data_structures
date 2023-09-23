"""Module providing an implementation for queue, using doubly-linked lists to store the elements."""

from typing import Any
from linked_lists.doubly_linked_list import DoublyLinkedList 

class Queue:
    """ A class modeling the queue container.
    """

    def __init__(self):
        """ Creates an empty linked_list.
        """
        self._data = DoublyLinkedList()


    def __len__(self):
        """
        Return the size of the queue.

        Parameters:
            None

        Returns:
            int: The number of values stored in the queue.
        """
        return len(self._data)



    def __iter__(self):
        """ Iterates on the elements of a queue.
            Warning: by doing so, the queue will be emptied.
        """
        while not self.is_empty():
            yield self.dequeue()


    def __str__(self):
        """
        Return the string representation of the queue.

        Parameters:
            None

        Returns:
            str: The string representation of the queue.
        """
        return str(self._data)


    def __repr__(self):
        """
        Return the string (internal) representation of the queue.

        Parameters:
            None

        Returns:
            str: The string representation of the queue.
        """
        return f'Queue({str(self._data)})'


    def is_empty(self) -> bool:
        """
        Check if the queue is empty.

        Parameters:
            None

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return self._data.is_empty()


    def enqueue(self, value: Any) -> None:
        """
        Add a new value to the rear of the queue.

        Parameters:
            value (Any): The value to insert into the queue.

        Returns:
            None
        """
        self._data.insert_to_back(value)


    def dequeue(self) -> Any:
        """
        Remove and return the last value added to the queue.

        Parameters:
            None

        Returns:
            Any: The value removed from the queue.

        Raises:
            ValueError: If the queue is empty.
        """
        if self.is_empty():
            raise ValueError("Cannot dequeue from an empty queue")
        return self._data.delete_from_front()
