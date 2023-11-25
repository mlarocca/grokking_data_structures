from math import floor, sqrt
from decimal import Decimal
from linked_lists.singly_linked_list import SinglyLinkedList

class HashTable:
    """ A hash table with chaining implementation.
    """

    __A__ = Decimal((sqrt(5) - 1) / 2)

    def __init__(self, buckets) -> None:
        self.m = buckets
        self._data = [SinglyLinkedList() for _ in range(buckets)]


    def __len__(self):
        """ Return the size of the hash table.
        """
        return sum((len(bucket) for bucket in self._data))


    def _hash(self, key):
        """ Computes the index in this hash table associated with a key.
        """
        return floor(abs(self.m * ((hash(key) * HashTable.__A__) % 1)))


    def _search(self, value):
        """ Search for a value in the hash table.
        """
        index = self._hash(value)
        return self._data[index]._search(value)


    def insert(self, value):
        """ Insert a value in the hash table.
        """
        index = self._hash(value)
        self._data[index].insert_in_front(value)


    def contains(self, value):
        """ Check if a value is in the hash table.
        """
        return self._search(value) is not None


    def delete(self, value):
        """ Delete a value from the hash table.
        """
        index = self._hash(value)
        try: 
            self._data[index].delete(value)
        except ValueError as exc:
            raise ValueError(f'No element with value {value} was found in the hash table.') from exc
