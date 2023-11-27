from math import floor, sqrt
from decimal import Decimal
from typing import Any, Callable
from linked_lists.singly_linked_list import SinglyLinkedList

class HashTable:
    """ A hash table with chaining implementation.
    """

    __A__ = Decimal((sqrt(5) - 1) / 2)

    def __init__(self, buckets: int, extract_key:  Callable[..., Any]=hash) -> None:
        if buckets <= 0:
            raise ValueError(f'Invalid size for the hash table (must be positive): {buckets}')
        self.m = buckets
        self._data = [SinglyLinkedList() for _ in range(buckets)]
        self._extract_key = extract_key


    def __len__(self):
        """ Return the size of the hash table.
        """
        return sum((len(bucket) for bucket in self._data))


    def _hash(self, key):
        """ Computes the index in this hash table associated with a key.
        """
        return floor(abs(self.m * ((Decimal(key) * HashTable.__A__) % 1)))


    def is_empty(self):
        """ Check if the hash table is empty.
        """
        return len(self) == 0


    def search(self, key):
        """
        Search for a value with the given key in the hash table.
        
        This is an internal method used to find the index and bucket for a key, 
        and then search in that bucket's linked list for the key.
        
        Parameters:
            key: The key to search for.
        
        Returns:
            The value associated with the key if found, None otherwise.
        """
        index = self._hash(key)
        return self._data[index].search(lambda x: self._extract_key(x) == key)


    def insert(self, value):
        """ Insert a value in the hash table.

            Parameters:
                value: The value to check add to the hash table.
        """
        index = self._hash(self._extract_key(value))
        self._data[index].insert_in_front(value)


    def contains(self, value):
        """ Check if a value is in the hash table.

            Parameters:
                value: The value to check for existence in the hash table.
            
            Returns: 
            True if the value is found in the hash table, False otherwise.
        """
        return self.search(self._extract_key(value)) is not None


    def delete(self, value):
        """ Delete a value from the hash table.

            Parameters:
                value: The value to be deleted from the hash table.
        """
        index = self._hash(self._extract_key(value))
        try: 
            self._data[index].delete(value)
        except ValueError as exc:
            raise ValueError(f'No element with value {value} was found in the hash table.') from exc
