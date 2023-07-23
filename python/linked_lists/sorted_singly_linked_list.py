from typing import Any
from .singly_linked_list import SinglyLinkedList

class SortedSinglyLinkedList(SinglyLinkedList):
    """ A sorted version of the singly-linked lists.
    """
    def insert_in_front(self, data: Any) -> None:
        raise NotImplementedError('This method is not available for sorted lists')


    def insert_to_back(self, data: Any) -> None:
        raise NotImplementedError('This method is not available for sorted lists')

    def insert(self, new_data: Any) -> None:
        """
        Insert a new value into the sorted singly linked list.

        Parameters:
            new_data (Any): The new data value to insert.

        Returns:
            None                
        """
        current = self._head
        previous = None
        while current is not None:
            if current.data() >= new_data:
                if previous is None:
                    self._head = SinglyLinkedList.Node(new_data, current)    # Add the element at the beginning of the list
                else:
                    previous.append(SinglyLinkedList.Node(new_data, current))    # General case
                return
            previous = current
            current = current.next()
        if previous is None:
            self._head = SinglyLinkedList.Node(new_data)    # The list is empty
        else:
            previous.append(SinglyLinkedList.Node(new_data, None))    # Add the element at the end of the list
