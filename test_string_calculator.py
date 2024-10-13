import unittest
from string_calculator import StringCalculator


class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = StringCalculator()

    
    def test_empty_string(self):
        self.assertEqual(self.calculator.add(""), 0)



if __name__ == "__main__":
    unittest.main()
