import unittest
from selection_sort import selectionSort
class SortTestCases(unittest.TestCase):

    def setUp(self):
        self.test_cases = [
            ([],[]),
            ([9,8,7,6,5,4,3,100,0,95,20,2],[0,2,3,4,5,6,7,8,9,20,95,100])
        ]
        
    def test_sort(self):
        for input_data, output_data in self.test_cases:
            selection_sort_output = selectionSort(input_data.copy())
            self.assertEqual(output_data, selection_sort_output)

unittest.main()
            