import unittest
from merge_sort import mergeSort

class SortTestCase(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([], []),
            ([12, 11, 13, 5, 6], [5, 6, 11, 12, 13]),
        ]
    
    def test_sort(self):
        for input_data, output_data in self.test_cases:
            mergeSort_output = mergeSort(input_data.copy(), 0, len(input_data) - 1)
            self.assertEqual(mergeSort_output, output_data)

unittest.main()