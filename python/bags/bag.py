"""Module providing an implementation for bag."""

from typing import Any
from linked_lists.singly_linked_list import SinglyLinkedList

class Bag:
    """ A class modeling the bag container.
    """
    def __init__(self) -> None:
        """ Creates an empty bag.
        """
        self._data = SinglyLinkedList()


    def __iter__(self):
        """
        Iterate over the values in the bag.

        Parameters:
            None

        Returns:
            Iterator: An iterator over the values in the bag.
        """

        return iter(self._data)


    def __len__(self):
        """
        Return the size of the bag.

        Parameters:
            None

        Returns:
            int: The number of values stored in the bag.
        """
        return len(self._data)


    def __str__(self):
        """
        Return the string representation of the bag.

        Parameters:
            None

        Returns:
            str: The string representation of the bag.
        """
        return str(','.join(map(str, self)))


    def __repr__(self):
        """
        Return the string (internal) representation of the bag.

        Parameters:
            None

        Returns:
            str: The string representation of the bag.
        """
        return f'Bag({",".join(map(str, self))})'


    def is_empty(self) -> bool:
        """
        Check if the bag is empty.

        Parameters:
            None

        Returns:
            bool: True if the bag is empty, False otherwise.
        """

        return self._data.is_empty()


    def insert(self, value: Any) -> None:
        """
        Insert a new value into the bag.

        Parameters:
            value (Any): The value to insert into the bag.

        Returns:
            None
        """
        self._data.insert_in_front(value)
