class StringCalculator:

    def add(self, numbers):
        # If not numbers, return 0
        if not numbers:
            return 0

        # Returns the sum of numbers
        nums = [int(num) for num in numbers.split(",")]
        return sum(nums)
