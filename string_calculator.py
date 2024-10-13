import re


class StringCalculator:

    def add(self, numbers: str) -> int:
        # If not numbers, return 0
        if not numbers:
            return 0

        # Setting up delimiter as there can be other than ","
        if numbers.startswith("//"):
            delimiter, numbers = numbers.split('\n', 1)
            delimiter = f"[{delimiter[2:]}\n]"
        else:
            delimiter = "[,\n]"

        # Calculation the sum of numbers
        nums = [int(num) for num in re.split(delimiter, numbers)]
        
        # Checking for negative values, and raising errors if so
        negatives = [num for num in nums if num < 0]
        if negatives:
            raise ValueError(f"Negative numbers are not allowed: {', '.join(map(str, negatives))}")
        
        return sum(nums)


if __name__ == "__main__":
    calculator = StringCalculator()
    print(calculator.add(numbers="//;\n1;2\n2;3"))