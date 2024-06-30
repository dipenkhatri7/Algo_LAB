import unittest
from bubble_sort import bubbleSort

class SortingTestCase(unittest.TestCase):
    
    def setUp(self):
        self.test_cases = [
            ([], []), # Test case with an empty list
            ([12, 11, 13, 5, 6], [5, 6, 11, 12, 13]), # Test case with a list of integers
        ]
    
    def test_sort(self):
        
        for input_data, expected_output in self.test_cases:
            sorted_bubble = bubbleSort(input_data.copy()) 
            self.assertEqual(sorted_bubble, expected_output)

unittest.main()