import unittest
from merge_sort import merge_sort # Importing merge sort function
from quick_sort import quick_sort # Importing quick sort function

class SortingTestCase(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([], []), # Test case with an empty list
            ([12, 11, 13, 5, 6], [5, 6, 11, 12, 13]), # Test case with a list of integers
            ([4, 2, 5, 3, 1], [1, 2, 3, 4, 5]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), # Test case for an already sorted list
            ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]), # Test case for a reverse sorted list
        ]

    def test_sort(self):
        for input_data, expected_output in self.test_cases:
            with self.subTest(input_data=input_data):
                sorted_merge = merge_sort(input_data.copy(), 0, len(input_data) - 1) # Sort using merge sort
                sorted_quick = quick_sort(input_data.copy(), 0, len(input_data) - 1) # Sort using quick sort

                self.assertEqual(sorted_merge, expected_output) # Check merge sort result
                self.assertEqual(sorted_quick, expected_output) # Check quick sort result

unittest.main() # Run the test suite
