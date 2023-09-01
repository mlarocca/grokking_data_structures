import arrays.core as core
from typing import Union

class SortedArray:
    '''Return a new sorted array whose items are restricted by typecode, and
       that can contain at most `max_size` elements.
       
       Arrays represent basic values and behave very much like Python list, except
       the type of objects stored in them is constrained. The type is specified
       at object creation time by using a type code, which is a single character.
       The following type codes are defined:
       
           Type code   C Type             Minimum size in bytes
           'b'         signed integer     1
           'B'         unsigned integer   1
           'u'         Unicode character  2
           'h'         signed integer     2
           'H'         unsigned integer   2
           'i'         signed integer     2
           'I'         unsigned integer   2
           'l'         signed integer     4
           'L'         unsigned integer   4
           'q'         signed integer     8
           'Q'         unsigned integer   8
           'f'         floating point     4
           'd'         floating point     8

        Parameters:
            max_size (int): The maximum number of elements the array can hold.
            typecode (str, optional): The typecode of the array. Defaults to 'l' for int.

       '''
    def __init__(self, max_size: int, typecode: str = 'l'):
        self._array = core.Array(max_size, typecode)
        self._max_size = max_size
        # The actual number of elements stored in the array
        self._size = 0

    
    def __len__(self) -> int:
        '''
        Return the number of elements in the array.

        Parameters:
            None

        Returns:
            int: The number of elements in the array.
        '''

        return self._size


    def __getitem__(self, index) -> Union[int, float]:
        '''
        Get the value at the given index.

        Parameters:
            index (int): The index to get the value from.

        Returns:
            Union[int, float]: The value at the given index.
        '''

        if index < 0 or index >= self._size:
            raise IndexError(f'Index out of bound: {index}')
        return self._array[index]


    def __repr__(self) -> str:
        '''
        Return the string representation of the array.

        Parameters:
            None

        Returns:
            str: The string representation of the array.
        '''

        return f'SortedArray({repr(self._array._array[:self._size])})'
    

    def __iter__(self):
        '''
        Iterate over the values in the sorted array.

        Parameters:
            None

        Functionality:
            Iterates over the values in the sorted array. The iteration starts at index 0 and
            goes on until it reaches the end of the array (not the full maximum capacity of the array,
            just the last stored elements).
        '''

        for i in range(self._size):
            yield self._array[i]


    def max_size(self) -> int:
        '''
        Return the number of elements that the array can hold.

        Parameters:
            None

        Returns:
            int: The maximum size of the array.

        '''

        return self._max_size


    def insert(self, value: Union[int, float]) -> None:
        '''
        Insert a new value into the sorted array.

        Parameters:
            value (any): The value to insert into the sorted array.

        Returns:
            None

        Functionality:
            Inserts the given value into the sorted array while maintaining the sorted order.
            If the array is already full, raises a ValueError.
            Otherwise, shifts elements to the right to make room for the new value and inserts 
            it in the correct position to keep the array sorted.
        '''

        if self._size >= self._max_size:
            raise ValueError(f'The array is already full, maximum size: {self._max_size}')
        for i in range(self._size, 0, -1):
            if self._array[i-1] <= value:
                # Found the right place for the element
                self._array[i] = value
                self._size += 1
                return
            else:
                self._array[i] = self._array[i-1]
        # If it gets here, it means we need to add the new value as the first entry
        self._array[0] = value
        self._size += 1
        
    
    def linear_search(self, target: Union[int, float]) -> Union[int, None]:
        '''
        Search for a target value in the sorted array using a naive linear search.

        Parameters:
            target (any): The value to search for in the sorted array.

        Returns:
            int or None: The index of the target value if found, otherwise None.

        Functionality:
            Performs a linear search over the values in the sorted array.
            Since the array is sorted, we can stop searching once we pass the point 
            where the target value would be located.
            Returns the index of the target value if found, otherwise returns None.
        '''

        for i in range(self._size):
            if self._array[i] == target:
                return i
            elif self._array[i] > target:
                # The array is sorted, we can't find the target in the rest of the array
                return None
        # Element not found, reached the end of the array
        return None


    def binary_search(self, target: Union[int, float]) -> Union[int, None]:
        '''
        Search for a target value in the sorted array using binary search.

        Parameters:
            target (any): The value to search for in the sorted array.

        Returns:
            int or None: The index of the target value if found, otherwise None.

        Functionality:
            Performs a binary search on the sorted array.
            Keeps track of left and right indices, and calculates the midpoint index.
            Checks if the midpoint value matches the target. If so, returns the midpoint index.
            Otherwise, recurses on either the left or right half of the array depending on if the 
            midpoint value is greater than or less than the target.
            Returns the index if found, otherwise returns None if the target is not found.
        '''

        left = 0
        right = self._size - 1
        while left <= right:
            mid_index = (left + right) // 2
            mid_val = self._array[mid_index]
            if mid_val == target:
                return mid_index
            elif mid_val > target:
                right = mid_index - 1
            else: 
                left = mid_index + 1
        return None

    def delete(self, target: Union[int, float]) -> None:
        '''
        Delete a target value from the sorted array.

        Parameters:
            target (any): The value to delete from the sorted array.

        Returns:
            None

        Functionality:
            Finds the index of the target value using the find method.
            If the target is not found, raises a ValueError.
            Otherwise, shifts all elements after the target to the left to fill in the gap.
            If it succeeds, it decrements the size of the array by 1.
        '''

        index = self.binary_search(target)
        if index is None:
            raise ValueError(f'Unable to delete element {target}: the entry is not in the array')

        # Must shift all the elements after the position of the target
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._size -= 1
