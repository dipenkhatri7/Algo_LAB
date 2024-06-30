import unittest
from sum import sum

class TestSum(unittest.TestCase):
    def test_sum(self):
        input_data = [1, 2, 3, 4, 5]
        res = sum(input_data)
        self.assertEqual(res, 15)
        
        input_data = []
        res = sum(input_data)
        self.assertEqual(res,0)
        

if __name__ == '__main__':
    unittest.main()