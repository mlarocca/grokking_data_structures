"""Module providing an implementation for doubly-linked list."""
from __future__ import annotations
import copy
from typing import Any, Callable, List, Optional

class DoublyLinkedList:
    """
    This class models a doubly-linked list data structure.

    A doubly-linked list consists of nodes where each node has references 
    to both the next node and the previous node in the list.

    Functionality:

    - Stores nodes containing arbitrary data.
    - Supports common linked list operations like insertion, deletion search and traversal.
    """

    class Node:
        """
        A node in a doubly linked list. Each node contains data and 
        references to the next and previous nodes in the list.

        Attributes:

            data: The data held in the node. Can be any arbitrary object.
            _next: A reference to the next node in the list.
            _prev: A reference to the previous node in the list.
        """

        def __init__(self, data: Any) -> None:
            """
            Initialize a new Node object. The links to previous and next nodes are set to None,
            indicating the new node has no links yet, and forcing the use of the `append` and `prepend`
            methods (which will update references appropriately) to link to other nodes. 

            Parameters:

            - data (Any): The data for the node. Can be any arbitrary object.   
            """

            self._data = data
            self._next = None
            self._prev = None


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


        def next(self) -> DoublyLinkedList.Node:
            """
            Return the successor of the current node.

            Parameters:
                None

            Returns:
                Node: The next node in the doubly-linked list.
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


        def append(self, next_node: Optional[DoublyLinkedList.Node]) -> None:
            """
            Append a node to the current one.

            Parameters:
            next_node (Optional[Node]): The node to append after the current node, or
                                        `None` to indicate no successor.
            """

            self._next = next_node
            if next_node is not None:
                next_node._prev = self


        def prev(self) -> DoublyLinkedList.Node:
            """
            Return the predecessor of the current node.

            Parameters:
                None

            Returns:
                Node: The previous node in the doubly-linked list.
            """

            return self._prev



        def has_prev(self) -> bool:
            """
            Check if the node has a predecessor.

            Parameters:
                None

            Returns:
                bool: True if the node has a previous node, False otherwise.
            """

            return self._prev is not None


        def prepend(self, prev_node: Optional[DoublyLinkedList.Node]) -> None:
            """
            Prepend a node to the current one.

            Parameters:
            prev_node (Optional[Node]): The node to prepend before the current node, or
                                        `None` to indicate no predecessor.
            """

            self._prev = prev_node
            if prev_node is not None:
                prev_node._next = self


    # --- DoublyLinkedList methods ---


    def __init__(self) -> None:
        """
        Initialize a new empty DoublyLinkedList.

        Parameters:
            None

        Attributes:
            _head (Node): The head node of the list. Initialized to None.
        """

        self._head = None
        self._tail = None


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

        return f'DoublyLinkedList({"<->".join(self.traverse(repr))})'


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

        return '<->'.join(self.traverse(str))


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

        if self._head is None:
            self._tail = self._head = DoublyLinkedList.Node(data)
        else:
            old_head = self._head
            self._head = DoublyLinkedList.Node(data)
            self._head.append(old_head)


    def insert_to_back(self, data: Any) -> None:
        """
        Append a node to the end of the list.

        Parameters:
        - data (Any): The data for the new node to append.
        
        Warning: this method requires traversing a linear number (O(n))
        of nodes.
        """

        if self._tail is None:
            self._tail = self._head = DoublyLinkedList.Node(data)
        else:
            old_tail = self._tail
            self._tail = DoublyLinkedList.Node(data)
            self._tail.prepend(old_tail)


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


    def _search(self, target: Any) -> Optional[DoublyLinkedList.Node]:
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

        node = self._search(target)
        if node is None:
            raise ValueError(f'No element with value {target} was found in the list.')

        if node.prev() is None:
            # Delete node from front
            self._head = node.next()
            if self._head is None:
                # In case the list's head was the only element in the list
                self._tail = None
            else:
                self._head.prepend(None)
        elif node.next() is None:
            # Delete node from back
            self._tail = node.prev()
            # We know tail can't be None, because node.prev() != None
            self._tail.append(None)
        else:
            node.prev().append(node.next())
            del node


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
        if self._head is None:
            self._tail = None
        else:
            self._head.prepend(None)
        return data


    def delete_from_back(self) -> Any:
        """
        Delete the last node in the list and return the data it held.

        Parameters:
            None

        Returns:
            The data held by the node that was deleted from the back of the list.

        Error Handling:
            If the list is empty, raises a ValueError.
        """

        if self.is_empty():
            raise ValueError('Delete on an empty list.')
        data = self._tail.data()
        self._tail = self._tail.prev()
        if self._tail is None:
            self._head = None
        else:
            self._tail.append(None)
        return data
