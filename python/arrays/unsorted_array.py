from arrays.core import Array

def insert_in_unsorted_array(new_entry, array, size) -> int:
    '''
    Insert an entry into an unsorted array.

    Parameters:
        new_entry (Any): The entry to insert.
        array (Array): The array to insert into.
        size (int): The current number of elements in the array.

    Returns:
        int: The new current size of the array after insertion.
    '''

    if size >= len(array):
        raise(ValueError('The array is already full'))
    else:
        array[size] = new_entry
        return size + 1


def delete_from_unsorted_array(index, array, size) -> int:
    '''
    Delete an entry at the given index from an unsorted array.

    Parameters:
        index (int): The index of the entry to delete.
        array (Array): The array to delete from.
        size (int): The current number of elements in the array.

    Returns:
        int: The new current size of the array after deletion.
    '''

    if size == 0:
        raise(ValueError('Delete from an empty array'))
    elif index < 0 or index >= size:
        raise(ValueError(f'Index {index} out of range.'))
    else:
        array[index] = array[size-1]
        return size - 1


def find_in_unsorted_array(target, array, size) -> int:
    '''
    Find the index of a target entry in an unsorted array.

    Parameters:
        target (Any): The entry to search for.
        array (Array): The array to search.
        size (int): The current number of elements in the array.

    Returns:
        int: The index of the first occurrence of the target entry, if found, else None.
    '''

    if size < 0 or size > len(array):
        raise(ValueError(f'Invalid size {size}'))
    for index in range(0, size):
        if array[index] == target:
            return index
    # Couldn't find the target
    return None

def traverse_unsorted_array(array, size, callback):
    '''
    Traverse an unsorted array and call a callback function on each element.

    Parameters:
        array (Array): The array to traverse.
        size (int): The number of elements in the array.
        callback (function): The function to call on each element.
    '''

    for index in range(size):
        callback(array[index]) 


if __name__ == '__main__':
    array = Array(3)
    print(array)
    size = 0
    
    # size = delete_from_unsorted_array(4, array, size)

    size = insert_in_unsorted_array(4, array, size)
    print(array, size)
    size = insert_in_unsorted_array(11, array, size)
    # size = delete_from_unsorted_array(2, array, size)
    size = insert_in_unsorted_array(32, array, size)
    print(array, size)

    traverse_unsorted_array(array, size, print)

    # size = insert_in_unsorted_array(5, array, size)
    size = delete_from_unsorted_array(1, array, size)
    print(array, size)
    # size = delete_from_unsorted_array(4, array, size)
    size = delete_from_unsorted_array(1, array, size)
    size = delete_from_unsorted_array(0, array, size)
    print(array, size)

    