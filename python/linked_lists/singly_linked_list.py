"""Module providing an implementation for singly-linked list."""
from __future__ import annotations
import copy
from typing import Any, Callable, List, Optional

class SinglyLinkedList:
    """
    This class models a singly-linked list data structure.

    A singly-linked list consists of nodes where each node has a reference 
    to the next node in the list.

    Functionality:

    - Stores nodes containing arbitrary data.
    - Supports common linked list operations like insertion, deletion search and traversal.
    """

    class Node:
        """
        A node in a singly linked list. Each node contains data and 
        a reference to the next node.

        Attributes:

            data: The data held in the node. Can be any arbitrary object.
            _next: A reference to the next node in the list.
        """

        def __init__(self, data: Any, next_node: SinglyLinkedList.Node = None) -> None:
            """
            Initialize a new Node object.

            Parameters:

            - data (Any): The data for the node. Can be any arbitrary object.
            - next_node (Node, optional): The next Node in the list. Defaults to None.            
            """

            self._data = data
            self._next = next_node


        def __str__(self) -> str:
            """
            Return a string representation of the node's data.

            Parameters:
                None

            Returns:
                str: String representation of the node's data.
            """

            return str(self.data())


        def __repr__(self) -> str:
            """
            Return a string (internal) representation of the node's data.

            Parameters:
                None

            Returns:
                str: String representation of the node's data.
            """

            return repr(self.data())


        def data(self) -> Any:
            """
            Get the data stored in this node.

            Parameters:
                None

            Returns:
                Any: The data stored in this node. Can be any arbitrary object.
            """

            return self._data


        def next(self) -> SinglyLinkedList.Node:
            """
            Return the successor of the current node.

            Parameters:
                None

            Returns:
                Node: The next node in the singly-linked list.
            """

            return self._next


        def has_next(self) -> bool:
            """
            Check if the node has a successor.

            Parameters:
                None

            Returns:
                bool: True if the node has a next node, False otherwise.
            """

            return self._next is not None


        def append(self, next_node: Optional[SinglyLinkedList.Node]) -> None:
            """
            Append a node to the current one.

            Parameters:
            next_node (Optional[Node]): The node to append after the current node, or
                                        `None` to indicate no successor.
            """

            self._next = next_node


    # --- SinglyLinkedList methods ---


    def __init__(self) -> None:
        """
        Initialize a new empty SinglyLinkedList.

        Parameters:
            None

        Attributes:
            _head (Node): The head node of the list. Initialized to None.
        """

        self._head = None


    def __len__(self):
        """
        Return the length of the linked list.

        Parameters:
            None

        Returns:
            int: The number of nodes in the linked list.
        """

        return len(self.traverse(lambda x: x))


    def __repr__(self) -> str:
        """
        Return the string (internal) representation of the linked list.

        Parameters:
            None

        Returns:
            str: The string representation of the linked list nodes.
        """

        return f'SinglyLinkedList({"->".join(self.traverse(repr))})'


    def __str__(self) -> str:
        """
        Return the string representation of the linked list.

        Parameters:
            None

        Returns:
            str: The string representation of the linked list nodes.

        Functionality:
            Traverses the linked list using the traverse() method, 
            passing in repr() to convert each node to a string.
            Joins the node string representations with '->' and returns the result.
        """

        return '->'.join(self.traverse(str))


    def __iter__(self):
        '''
        Iterate over the values in the linked list.

        Parameters:
            None

        Functionality:
            Iterates over the values in the linked list. The iteration starts at the beginning
            of the list and goes on until it reaches the tail of the list.
        '''

        current = self._head
        while current is not None:
            data = current.data()
            current = current.next()
            yield data


    def size(self) -> int:
        """
        Return the length of the linked list.

        Parameters:
            None

        Returns:
            int: The number of nodes in the linked list.
        """

        size = 0
        current = self._head
        while current is not None:
            size += 1
            current = current.next()
        return size


    def is_empty(self) -> bool:
        """
        Check if the linked list is empty.

        Parameters:
            None

        Returns:
            bool: True if the linked list is empty, False otherwise.
        """

        return self._head is None


    def insert_in_front(self, data: Any) -> None:
        """
        Add a node to the beginning of the list.

        Parameters:
        - data (Any): The data for the new node to add.
        """

        old_head = self._head
        self._head = SinglyLinkedList.Node(data, old_head)


    def insert_to_back(self, data: Any) -> None:
        """
        Append a node to the end of the list.

        Parameters:
        - data (Any): The data for the new node to append.
        
        Warning: this method requires traversing a linear number (O(n))
        of nodes.
        """

        current = self._head
        if current is None:
            self._head = SinglyLinkedList.Node(data)
        else:
            while current.next() is not None:
                current = current.next()
            current.append(SinglyLinkedList.Node(data))


    def get(self, index):
        """
        Get the data at the given index.

        Parameters:
            index (int): The index of the element to retrieve, starting from the head of the list.
        
        Returns:
            Any: A deep copy of the data at the given index if found.
        
        Error Handling:
            Raising an IndexError if index is invalid.
        """
        if index < 0:
            raise IndexError("Index must be non-negative")
        current = self._head
        current_index = 0
        while current_index < index and current is not None:
            current = current.next()
            current_index += 1
        if current is None:
            raise IndexError("Index out of bounds")
        # Here we know that we are at the right index
        return copy.deepcopy(current.data())


    def traverse(self, functor: Callable[..., Any]) -> List[Any]:
        """
        Traverse the linked list and apply a function to each node's data.

        Parameters:
            functor (Callable): The function (or functor) to apply to each node's data.

        Returns:
            List[Any]: A list containing the result of applying the function 
                    to each node's data.
        """

        current = self._head
        result = []
        while current is not None:
            result.append(functor(current.data()))
            current = current.next()
        return result


    def _search(self, target: Any) -> Optional[SinglyLinkedList.Node]:
        """
        Search the list for a node with the data matching `target`, and return the node found.

        Parameters:
        - target (Any): The data to search for in the list.
        
        Returns:
        - Optional[Node]: The node containing the target data if found, 
                            otherwise None.
        """
        current = self._head
        while current is not None:
            if current.data() == target:
                return current
            current = current.next()
        return None


    def search(self, predicate:  Callable[..., Any]) -> Optional[Any]:
        """
        Search the list for the first node whose data matches the predicate function.
        
        Parameters:
            predicate (Callable): The predicate function to evaluate node data against.
                                Should accept a single parameter for the node data.
                                
        Returns:
            Optional[Any]: The first element for which predicate(element) is True, 
                        or None if no match is found.
        """
        current = self._head
        while current is not None:
            if predicate(current.data()):
                return current.data()
            current = current.next()
        return None


    def delete(self, target: Any) -> None:
        """
        Delete the first node with the given data from the list.

        Parameters:
            target (Any): The data value to delete from the list.

        Returns:
            None

        Error Handling:
            If no match is found after full traversal, raises a ValueError.
        """

        current = self._head
        previous = None
        while current is not None:
            if current.data() == target:
                if previous is None:
                    self._head = current.next()
                else:
                    previous.append(current.next())
                return
            previous = current
            current = current.next()
        # If it gets here, it hasn't found the target
        raise ValueError(f'No element with value {target} was found in the list.')


    def delete_from_front(self) -> Any:
        """
        Delete the first node in the list and return the data it held.

        Parameters:
            None

        Returns:
            The data held by the node that was deleted from the front.

        Error Handling:
            If the list is empty, raises a ValueError.
        """

        if self.is_empty():
            raise ValueError('Delete on an empty list.')
        data = self._head.data()
        self._head = self._head.next()
        return data
