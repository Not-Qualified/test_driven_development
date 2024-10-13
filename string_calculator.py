import re


class StringCalculator:

    def add(self, numbers):
        # If not numbers, return 0
        if not numbers:
            return 0

        # Calculation the sum of numbers
        nums = [int(num) for num in re.split("[,\n]", numbers)]
        
        # Checking for negative values, and raising errors if so
        negatives = [num for num in nums if num < 0]
        if negatives:
            raise ValueError(f"Negative numbers are not allowed: {', '.join(map(str, negatives))}")
        

        return sum(nums)
