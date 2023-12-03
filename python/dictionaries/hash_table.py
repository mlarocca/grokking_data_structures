from math import floor, sqrt
from decimal import Decimal
from typing import Any, Callable
from linked_lists.singly_linked_list import SinglyLinkedList

class HashTable:
    """ A hash table with chaining implementation.
    """

    __A__ = Decimal((sqrt(5) - 1) / 2)

    def __init__(self, buckets: int, extract_key:  Callable[..., Any]=hash) -> None:
        """ Create an empty hash table. Chaining is used for collision resolution.

        Parameters:
            buckets: The size of the hash table, that is, the number of hash chains.
                Note that the size of the hash table is not the number of elements it can store,
                which is unbounded.
                The size must be a positive integer.
            extract_key: A function that extracts the key from any value stored in the table.
                Note that, for the table to work properly, keys must be integers uniquely
                identifying the values stored in the table.
                If not given, the built-in `hash` function is used.

        """
        if buckets <= 0:
            raise ValueError(f'Invalid size for the hash table (must be positive): {buckets}')
        self._m = buckets
        self._data = [SinglyLinkedList() for _ in range(buckets)]
        self._extract_key = extract_key


    def __len__(self):
        """ Return the size of the hash table.
        """
        return sum((len(bucket) for bucket in self._data))


    def _hash(self, key: int):
        """ Computes the index in this hash table associated with a key.
        """
        return floor(abs(self._m * ((Decimal(key) * HashTable.__A__) % 1)))


    def is_empty(self) -> int:
        """ Check if the hash table is empty.
        """
        return len(self) == 0


    def search(self, key: int) -> Any:
        """
        Search for a value with the given key in the hash table.
        
        Parameters:
            key: The key to search for.
        
        Returns:
            The value associated with the key if found, None otherwise.
        """
        index = self._hash(key)
        value_matches_key = lambda v: self._extract_key(v) == key
        return self._data[index].search(value_matches_key)


    def insert(self, value: Any) -> None:
        """ Insert a value in the hash table.

            Parameters:
                value: The value to check add to the hash table.
        """
        index = self._hash(self._extract_key(value))
        self._data[index].insert_in_front(value)


    def contains(self, value: Any) -> bool:
        """ Check if a value is in the hash table.

            Parameters:
                value: The value to check for existence in the hash table.
            
            Returns: 
            True if the value is found in the hash table, False otherwise.
        """
        return self.search(self._extract_key(value)) is not None


    def delete(self, value: Any) -> None:
        """ Delete a value from the hash table.

            Parameters:
                value: The value to be deleted from the hash table.
        """
        index = self._hash(self._extract_key(value))
        try: 
            self._data[index].delete(value)
        except ValueError as exc:
            raise ValueError(f'No element with value {value} was found in the hash table.') from exc
