import unittest
from string_calculator import StringCalculator


class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = StringCalculator()

    
    def test_empty_string(self):
        self.assertEqual(self.calculator.add(""), 0)

    def test_single_number(self):
        self.assertEqual(self.calculator.add("1"), 1)
    
    def test_two_numbers(self):
        self.assertEqual(self.calculator.add("1,4"), 5)
    
    def test_multiple_numbers(self):
        self.assertEqual(self.calculator.add("1,2,3,4,5"), 15)


if __name__ == "__main__":
    unittest.main()
