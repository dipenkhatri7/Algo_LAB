import unittest
from heap_sort import heapSort
class SortTestCases(unittest.TestCase):
    
    def setUp(self):
        self.test_cases = [
            ([],[]),
            ([9,8,7,6,5,12,100,0], [0,5,6,7,8,9,12,100])
        ]
    
    def test_sort(self):
        for input_data, output_data in self.test_cases:
            insertion_output = heapSort(input_data.copy())
            self.assertEqual(insertion_output, output_data)

unittest.main()