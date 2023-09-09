from typing import Union
from arrays.core import Array

class UnsortedArray:
    '''Return a new unsorted array whose items are restricted by typecode, and
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
        self._array = Array(max_size, typecode)
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

        return f'UnsortedArray({repr(self._array._array[:self._size])})'


    def max_size(self) -> int:
        '''
        Return the number of elements that the array can hold.

        Parameters:
            None

        Returns:
            int: The maximum size of the array.

        '''

        return self._max_size


    def insert(self, new_entry) -> None:
        '''
        Insert an entry into an unsorted array.

        Parameters:
            new_entry (Any): The entry to insert.
        '''

        if self._size >= len(self._array):
            raise ValueError('The array is already full')
        else:
            self._array[self._size] = new_entry
            self._size += 1


    def delete(self, index) -> None:
        '''
        Delete an entry at the given index from an unsorted array.

        Parameters:
            index (int): The index of the entry to delete.
        '''

        if self._size == 0:
            raise ValueError('Delete from an empty array') 
        elif index < 0 or index >= self._size:
            raise ValueError(f'Index {index} out of range.') 
        else:
            self._array[index] = self._array[self._size-1]
            self._size -= 1


    def find(self, target) -> int:
        '''
        Find the index of a target entry in an unsorted array.

        Parameters:
            target (Any): The entry to search for.

        Returns:
            int: The index of the first occurrence of the target entry, if found, else None.
        '''

        for index in range(0, self._size):
            if self._array[index] == target:
                return index
        # Couldn't find the target
        return None

    def traverse(self, callback):
        '''
        Traverse an unsorted array and call a callback function on each element.

        Parameters:
            callback (function): The function to call on each element.
        '''

        for index in range(self._size):
            callback(self._array[index])
