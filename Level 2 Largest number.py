def find_largest(numbers):
    """
    Returns the largest number in a list.
    """
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest


# Example usage
nums = list(map(int, input("Enter numbers separated by space: ").split()))
print("Largest number is:", find_largest(nums))