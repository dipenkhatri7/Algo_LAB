import unittest
from knapsack import fractional_knapsack_brute_force, knapsack_01_brute_force, fractional_knapsack_greedy, dp_knapsack, recursive_knapsack

class KnapsackTestCase(unittest.TestCase):
    def setUp(self):
        self.test_cases_fractional = [
            ([60, 100, 120], [10, 20, 30], 50, 240.0),
            ([10, 40, 50, 70], [1, 3, 4, 5], 8, 110.0),
            ([], [], 10, 0),
            ([15], [10], 5, 7.5),
        ]
        
        self.test_cases_01 = [
            ([60, 100, 120], [10, 20, 30], 50, 220),
            ([10, 40, 50, 70], [1, 3, 4, 5], 8, 110),
            ([], [], 10, 0),
            ([15], [10], 5, 0),
        ]

    def test_fractional_knapsack_brute_force(self):
        for profit, weight, capacity, expected_output in self.test_cases_fractional:
            with self.subTest(profit=profit, weight=weight, capacity=capacity):
                result = fractional_knapsack_brute_force(profit, weight, capacity)
                self.assertAlmostEqual(result, expected_output, places=2, msg=f"Expected {expected_output} but got {result}")

    def test_knapsack_01_brute_force(self):
        for profit, weight, capacity, expected_output in self.test_cases_01:
            with self.subTest(profit=profit, weight=weight, capacity=capacity):
                result = knapsack_01_brute_force(profit, weight, capacity)
                self.assertEqual(result, expected_output, msg=f"Expected {expected_output} but got {result}")

    def test_fractional_knapsack_greedy(self):
        for profit, weight, capacity, expected_output in self.test_cases_fractional:
            with self.subTest(profit=profit, weight=weight, capacity=capacity):
                result = fractional_knapsack_greedy(profit, weight, capacity)
                self.assertAlmostEqual(result, expected_output, places=2, msg=f"Expected {expected_output} but got {result}")

    def test_dp_knapsack(self):
        for profit, weight, capacity, expected_output in self.test_cases_01:
            with self.subTest(profit=profit, weight=weight, capacity=capacity):
                result = dp_knapsack(profit, weight, capacity)
                self.assertEqual(result, expected_output, msg=f"Expected {expected_output} but got {result}")
                
    def test_recursive_knapsack(self):
        for profit, weight, capacity, expected_output in self.test_cases_01:
            with self.subTest(profit=profit, weight=weight, capacity=capacity):
                result = recursive_knapsack(profit, weight, capacity, len(profit))
                self.assertEqual(result, expected_output, msg=f"Expected {expected_output} but got {result}")

if __name__ == "__main__":
    unittest.main()
