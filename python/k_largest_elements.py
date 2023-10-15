from queues.heap import Heap

def k_largest_elements(arr, k):
    """Finds the k largest elements in an array (or as many as there are in the array if k > len(arr)).
       Returns a list of tuples, where each tuple is (index, value).
    """
    heap = Heap(element_priority=lambda x: -x[1])
    for i in range(len(arr)):
        if len(heap) >= k:
            if heap.peek()[1] < arr[i]:
                heap.top()  # remove the smallest element, we don't need the value
                heap.insert((i, arr[i]))
                heap._validate()
        else:
            heap.insert((i, arr[i]))
    return [heap.top() for _ in range(k)]

if __name__ == '__main__':
    arr = [55, 71, 43, 59, 10, 20, 15, 44, 11, 234, 23,-45]
    print(k_largest_elements(arr, 6))
