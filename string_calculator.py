class StringCalculator:

    def add(self, numbers):
        # If not numbers, return 0
        if not numbers:
            return 0

        # Returns the sum of numbers
        nums = [int(num) for num in numbers.split(",")]
        negatives = [num for num in nums if num < 0]

        if negatives:
            raise ValueError(f"Negative numbers are not allowed: {', '.join(map(str, negatives))}")
        
        return sum(nums)
