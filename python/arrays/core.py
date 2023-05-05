import array
from typing import Union

class Array():
    '''Return a new array whose items are restricted by typecode, and
         |  that can contain at most `size` elements.
         |  
         |  Arrays represent basic values and behave very much like lists, except
         |  the type of objects stored in them is constrained. The type is specified
         |  at object creation time by using a type code, which is a single character.
         |  The following type codes are defined:
         |  
         |      Type code   C Type             Minimum size in bytes
         |      'b'         signed integer     1
         |      'B'         unsigned integer   1
         |      'u'         Unicode character  2 (see note)
         |      'h'         signed integer     2
         |      'H'         unsigned integer   2
         |      'i'         signed integer     2
         |      'I'         unsigned integer   2
         |      'l'         signed integer     4
         |      'L'         unsigned integer   4
         |      'q'         signed integer     8 (see note)
         |      'Q'         unsigned integer   8 (see note)
         |      'f'         floating point     4
         |      'd'         floating point     8
         |  '''
    def __init__(self, size: int, typecode: str = 'l'):
        if size <= 0:
            raise(Exception(f'Invalid array size (must be positive): {size}'))
        self._size = size
        self._array = array.array(typecode, [0] * size)
    
    def __getitem__(self, key: int) -> Union[int, float]:
        """
        Get the value at the given index.

        Parameters:
            key (int): The index to get the value from.

        Returns:
            Union[int, float]: The value at the given index.
        """

        if key < 0 or key >= self._size:
            raise(Exception('array index out of range'))
        return self._array[key]
        
    def __setitem__(self, key: int, val: Union[int, float]) -> None:
        """
        Set the value at the given index.

        Parameters:
            key (int): The index to set the value at.
            val (Union[int, float]): The value to set.

        Returns:
            None
        """

        if key < 0 or key >= self._size:
            raise(Exception('array assignment index out of range'))
        self._array[key] = val
    
    def __len__(self):
        """
        Return the number of elements in the array.

        Parameters:
            None

        Returns:
            int: The number of elements in the array.
        """

        return self._size
    
    def __repr__(self):
        """
        Return the string representation of the array.

        Parameters:
            None

        Returns:
            str: The string representation of the array.
        """

        return self._array.__repr__()