"""Module providing an implementation for queue, using a statically-sized
   array to store the elements."""

from typing import Any

class Queue:
    """ A class modeling the queue container.
    """

    def __init__(self, max_size):
        """ Creates a static array with size `max_size`.
        """
        if max_size <= 1:
            raise ValueError(f'Invalid size (a queue must have at least two elements): {max_size}')
        self._data = [None] * max_size
        self._max_size = max_size
        self._front = 0
        self._rear = 0
        self._size = 0


    def __len__(self):
        """
        Return the size of the queue.

        Parameters:
            None

        Returns:
            int: The number of values stored in the queue.
        """
        return self._size


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
        def iterate():
            # We don't normally allow iterating on the elements of a queue without dequeueing them
            if self.is_empty():
                return
            front = self._front
            if front > self._rear:
                while front < self._max_size:
                    yield self._data[front]
                    front += 1
                front = 0
            while front < self._rear:
                yield self._data[front]
                front += 1

        return str([x for x in iterate()])


    def __repr__(self):
        """
        Return the string (internal) representation of the queue.

        Parameters:
            None

        Returns:
            str: The string representation of the queue.
        """
        return f'Queue({str(self)})'


    def is_empty(self) -> bool:
        """
        Check if the queue is empty.

        Parameters:
            None

        Returns:
            bool: True if the queue is empty, False otherwise.
        """
        return len(self) == 0



    def is_full(self) -> bool:
        """
        Check if the queue is full.

        Parameters:
            None

        Returns:
            bool: True if the queue is full, False otherwise.
        """
        return len(self) == self._max_size


    def enqueue(self, value: Any) -> None:
        """
        Add a new value to the rear of the queue.

        Parameters:
            value (Any): The value to insert into the queue.

        Returns:
            None
        """
        if self.is_full():
            raise ValueError('The queue is already full!')
        self._data[self._rear] = value
        self._rear = (self._rear + 1) % self._max_size
        self._size += 1


    def dequeue(self) -> Any:
        """
        Remove and return the oldest value added to the queue.

        Parameters:
            None

        Returns:
            Any: The value removed from the queue.

        Raises:
            ValueError: If the queue is empty.
        """
        if self.is_empty():
            raise ValueError("Cannot dequeue from an empty queue")

        value = self._data[self._front]
        self._front = (self._front + 1) % self._max_size
        self._size -= 1
        return value
