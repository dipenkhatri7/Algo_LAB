import unittest
from quick_sort import quickSort

class SortTestCase(unittest.TestCase):
    
    def setUp(self):
        self.test_cases = [
            ([],[]),
            ([9,8,7,6,5,4,3,2,0],[0,2,3,4,5,6,7,8,9])
        ]
    
    def test_sort(self):
        for input_data, output_data in self.test_cases:
            quick_sort_output = quickSort(input_data, 0, len(input_data) - 1)
            self.assertEqual(quick_sort_output, output_data)
    
unittest.main()