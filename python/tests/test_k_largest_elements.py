import unittest
from k_largest_elements import k_largest_elements

class TestKLargestElements(unittest.TestCase):

    def test_k_smaller_than_array(self):
        arr = [55, 71, 43, 59, 10, 20, 15, 44, 11, 234, 23, -45]
        result = k_largest_elements(arr, 3)
        self.assertCountEqual([v for _, v in result], [234, 71, 59])
        for i, v in result:
            self.assertEqual(arr[i], v)

    def test_k_larger_than_array(self):
        # As documented: returns as many elements as there are in the array
        result = k_largest_elements([5, 1, 9], 5)
        self.assertCountEqual(result, [(0, 5), (1, 1), (2, 9)])

    def test_empty_array(self):
        self.assertListEqual(k_largest_elements([], 3), [])

if __name__ == '__main__':
    unittest.main()
