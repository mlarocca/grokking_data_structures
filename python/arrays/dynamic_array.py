import arrays.core as core
from typing import Union

class DynamicArray:
    '''Return a new dynamic _unsorted_ array whose items are restricted by typecode.
       The initial capacity of the array is by default 1, but this can be changed
       by passing a value for the initial_capacity argument.

       This array is not limited in the number of elements they can store, it will
       seamlessly expand and shrink automatically when needed.
       The initial capacity can be set, however, to optimize initial allocation, if
       the user knows the approximate number of elements that will be needed.
       
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
            initial_capacity (int, optional): The maximum number of elements the array can hold.
            typecode (str, optional): The typecode of the array. Defaults to 'l' for int.

       '''
    def __init__(self, initial_capacity: int = 1, typecode: str = 'l') -> None:
        self._array = core.Array(initial_capacity, typecode)
        self._capacity = initial_capacity
        self._size = 0
        self._typecode = typecode


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

        if index >= self._size:
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

        return repr(self._array._array[:self._size])    


    def __iter__(self):
        '''
        Iterate over the values in the sorted array.

        Parameters:
            None

        Functionality:
            Iterates over the values in the unsorted array. The iteration starts at index 0 and
            goes on until it reaches the last element in the array.
        '''

        for i in range(self._size):
            yield self._array[i]


    def _is_full(self):
        '''Check if the array is full.

        Parameters: None

        Returns: bool: True if the array is full, False otherwise.

        Functionality: Checks if the size of the array is greater than or equal to the capacity.
        Returns True if so, False otherwise.
        '''

        return self._size >= self._capacity
    
    
    def _double_size(self):
        '''
        Double the size of the underlying static array.

        Parameters: 
            None

        Functionality:
            Creates a new array with double the capacity of the old one.
            Copies all elements from the old array into the new larger array.
        '''

        assert(self._capacity  == self._size)   # Invariant: this is called only when capacity == size
        old_array = self._array
        self._array = core.Array(self._capacity * 2, self._typecode)
        self._capacity *= 2
        for i in range(self._size):
            self._array[i] = old_array[i]

        assert(self._array._size == self._capacity) # Invariant: the size of the new static array should be equal to the new capacity


    def _halve_size(self):
        '''
        Resize the static array to half the capacity.

        Parameters: 
            None

        Functionality:
            Halves the size of the underlying static array.

            Creates a new array with half the capacity of the old one.
            Copies all elements from the old array into the new smaller array.
        '''

        assert(self._capacity > 1 and self._size <= self._capacity/4) # Invariant: this is called only when capacity > 1 and size <= capacity/4
        old_array = self._array
        self._array = core.Array(self._capacity // 2, self._typecode)
        self._capacity //= 2
        for i in range(self._size):
            self._array[i] = old_array[i]

        assert(self._array._size == self._capacity) # Invariant: the size of the new static array should be equal to the new capacity


    def is_empty(self):
        '''
        Check if the array is empty.

        Parameters: 
            None

        Returns: 
            bool: True if the array is empty, False otherwise.

        Functionality:
            Checks if no elements is stored in the array. Returns True if so, False otherwise.
        '''   

        return len(self) == 0


    def insert(self, value: Union[int, float]) -> None:
        '''
        Insert a new value into the unsorted array.

        Parameters:
            value (any): The value to insert into the sorted array.

        Returns:
            None

        Functionality:
            Inserts the given value into the unsorted array.
            The new element is added at the end of the array.
        '''

        if self._is_full():
            self._double_size()

        # By now, we are sure that self._size < len(self._array)
        self._array[self._size] = value
        self._size += 1


    def find(self, target: Union[int, float]) -> Union[int, None]:
        '''
        Search for a target value in the unsorted array.

        Parameters:
            target (any): The value to search for in the sorted array.

        Returns:
            int or None: The index of the target value if found, otherwise None.

        Functionality:
            Performs a linear search over the values in the sorted array.
            Returns the index of the leftmost occurrence of the target value, if found.
            Otherwise returns None.
        '''

        for i in range(self._size):
            if self._array[i] == target:
                return i
        # Element not found, reached the end of the array
        return None


    def delete(self, target: Union[int, float]) -> None:
        '''
        Delete a target value from the array.

        Parameters:
            target (any): The value to delete from the sorted array.

        Returns:
            None

        Functionality:
            Finds the leftmost index of the target value using the find method.
            If the target is not found, raises a ValueError.
            Otherwise, deletes the target value by shifting all values after it to the left,
            to keep the remaining elements in the order they were inserted.
        '''

        index = self.find(target)
        if index is None:
            raise ValueError(f'Unable to delete element {target}: the entry is not in the array')

        # Must shift all the elements after the position of the target
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]
        self._size -= 1    

        # Check if we should shrink the array
        if self._capacity > 1 and self._size <= self._capacity/4:
            self._halve_size()
