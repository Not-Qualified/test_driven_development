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
    
    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as error:
            self.calculator.add("1,-3,-4,-5,-6,8,9")
        self.assertEqual(str(error.exception), "Negative numbers are not allowed: -3, -4, -5, -6")

    def test_new_line_between_numbers(self):
        self.assertEqual(self.calculator.add("1\n2,3\n5"), 11)

if __name__ == "__main__":
    unittest.main()
