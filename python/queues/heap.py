from typing import Any, List, Optional

class Heap:
    """ Implementation of a binary heap.
        The heap is a max-heap, meaning that the element with the highest priority is at the root.
        The priority of an element, however, can be computed using a function passed
        as an argument to the constructor.
    """

    def __init__(self, elements: List[Any] = None, element_priority = lambda x: x) -> None:
        """Constructor for the heap.

        Args:
            elements: The elements for initializing the heap. By default, the heap is empty.
            element_priority: A function that extracts the priority of an element. 
                              By default, the priority is the element itself.
        """
        self._priority = element_priority
        if elements is not None and len(elements) > 0:
            self._heapify(elements)
        else:
            self._elements = []


    def __len__(self) -> int:
        """Size of the heap.

        Returns: The number of elements in the heap.
        """
        return len(self._elements)


    def _has_lower_priority(self, element_1: Any, element_2: Any) -> bool:
        """Checks if the first element has lower priority to the second element."""
        return self._priority(element_1) < self._priority(element_2)


    def _has_higher_priority(self, element_1: Any, element_2: Any) -> bool:
        """Checks if the first element has higher priority to the second element."""
        return self._priority(element_1) > self._priority(element_2)


    def _validate(self) -> bool:
        """Checks that the three invariants for heaps are abided by.
        1.	Every node has at most 2 children. (Guaranteed by construction)
        2.	The heap tree is complete and left-adjusted.(Also guaranteed by construction)
        3.	Every node holds the highest priority in the subtree rooted at that node.

        Returns: True if all the heap invariants are met.
        """
        current_index = 0
        first_leaf = self._first_leaf_index()
        while current_index < first_leaf:
            current_element: float = self._elements[current_index]
            first_child = self._left_child_index(current_index)
            last_child_guard = min(first_child + 2, len(self))
            for child_index in range(first_child, last_child_guard):
                if self._has_lower_priority(current_element,  self._elements[child_index]):
                    return False    # pragma: no cover
            current_index += 1
        return True


    def _left_child_index(self, index) -> int:
        """Computes the index of the left child of a heap node.

        Args:
            index: The index of current node, for which we need to find children's indices.

        Returns: The index of the left-most child for current heap node.
        """
        return index * 2 + 1


    def _parent_index(self, index: int) -> int:
        """Computes the index of the parent of a heap node.

        Args:
            index: The index of current node, for which we need to find its parent's indices.

        Returns: The index of the parent of current heap node.

        """
        return (index - 1) // 2


    def _highest_priority_child_index(self, index: int) -> Optional[int]:
        """Finds, among the children of a heap node, the one child with highest priority.
        In case multiple children have the same priority, the left-most is returned.

        Args:
            index: The index of the heap node whose children are searched.

        Returns: The index of the child of current heap node with highest priority, or None if
                 current node has no child.
        """
        first_index = self._left_child_index(index)

        if first_index >= len(self):
            # The current element has no children
            return None

        if first_index + 1 >= len(self):
            # The current element only has one child
            return first_index

        if self._has_higher_priority(self._elements[first_index], self._elements[first_index + 1]):
            return first_index
        else:
            return first_index + 1


    def _first_leaf_index(self):
        """Computes the index of the first leaf of the heap.
           A leaf is the first node that has no children.
           For a binary heap, we know that's exactly the node in the middle of the array.
        """
        return len(self) // 2


    def _push_down(self, index: int) -> None:
        """Pushes down the root of a sub-heap towards its leaves to reinstate heap invariants.
        If any of the children of the element has a higher priority, then it swaps current
        element with its highest-priority child C, and recursively checks the sub-heap previously 
        rooted at that C.

        Args:
            index: The index of the root of the sub-heap.
        """

        # INVARIANT: 0 <= index < n
        assert 0 <= index < len(self._elements)
        element = self._elements[index]
        current_index = index
        while True:
            child_index = self._highest_priority_child_index(current_index)
            if child_index is None:
                break
            if self._has_lower_priority(element, self._elements[child_index]):
                self._elements[current_index] = self._elements[child_index]
                current_index = child_index
            else:
                break

        self._elements[current_index] = element


    def _bubble_up(self, index: int) -> None:
        """Bubbles up towards the root an element, to reinstate heap's invariants.
        If the parent P of an element has lower priority, then swaps current element and its parent,
        and then recursively check the position previously held by the P.

        Args:
            index: The index of the element to bubble up.
        """
        # INVARIANT: 0 <= index < n
        assert 0 <= index < len(self._elements)
        element = self._elements[index]
        while index > 0:
            parent_index = self._parent_index(index)
            parent = self._elements[parent_index]
            if self._has_higher_priority(element, parent):
                self._elements[index] = parent
                index = parent_index
            else:
                break

        self._elements[index] = element


    def _heapify(self, elements: List[Any]) -> None:
        """Initializes the heap with a list of elements and priorities.

        Args:
            elements: The list of elements to add to the heap.
            priorities: The priorities for those elements (in the same order they are presented).
        """
        self._elements = elements[:]
        last_inner_node_index = self._first_leaf_index() - 1
        for index in range(last_inner_node_index, -1, -1):
            self._push_down(index)


    def is_empty(self) -> bool:
        """Checks if the heap is empty.

        Returns: True if the heap is empty.

        """
        return len(self) == 0


    def top(self) -> Any:
        """Removes and returns the highest-priority element in the heap.
        If the heap is empty, raises a `ValueError`.

        Returns: The element with highest priority in the heap.
        """
        if self.is_empty():
            raise ValueError('Method top called on an empty heap.')
        if len(self) == 1:
            element = self._elements.pop()
        else:
            element = self._elements[0]
            self._elements[0] = self._elements.pop()
            self._push_down(0)

        return element


    def peek(self) -> Any:
        """Returns, WITHOUT removing it, the highest-priority element in the heap.
        If the heap is empty, raises a `ValueError`.

        Returns: A reference to the element with highest priority in the heap.
        """
        if self.is_empty():
            raise ValueError('Method peek called on an empty heap.')
        return self._elements[0]


    def insert(self, element: Any) -> None:
        """Add a new element/priority pair to the heap

        Args:
            element: The new element to add.
            priority: The priority associated with the new element
        """
        self._elements.append(element)
        self._bubble_up(len(self._elements) - 1)
