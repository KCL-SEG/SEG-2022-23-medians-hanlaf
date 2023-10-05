"""Median calculator."""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]

        # Work out the median
        numbers.sort()

        if len(numbers) % 2 == 0:
            # The list is even, so we want the middle positions

            leftPos = (len(numbers) - 1) // 2
            rightPos = (len(numbers) + 1) // 2
            median = (numbers[leftPos] + numbers[rightPos]) / 2
            print(float(median))
        else:
            # The list is odd, so we want the middle position
            medianPos = int((len(numbers) - 1) / 2)
            print(float(numbers[medianPos]))

    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break