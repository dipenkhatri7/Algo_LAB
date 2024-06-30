import unittest
from insertion_sort import insertionSort # Importing insertion sort function
from selection_sort import selectionSort # Importing selection sort function

class SortingTestCase(unittest.TestCase):
    def setUp(self):
        self.test_cases = [
            ([], []), # Test case with an empty list
            ([12, 11, 13, 5, 6], [5, 6, 11, 12, 13]), # Test case with a list of integers
        ]

    def test_sort(self):
        for input_data, expected_output in self.test_cases:
            sorted_insertion = insertionSort(input_data.copy()) # Sort using insertion sort
            sorted_selection = selectionSort(input_data.copy()) # Sort using selection sort
            self.assertEqual(sorted_insertion, expected_output) # Check insertion sort result
            self.assertEqual(sorted_selection, expected_output) # Check selection sort result

unittest.main() # Run the test suite
