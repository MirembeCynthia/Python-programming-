def find_largest_number(numbers):
    if not numbers:
        return None  # Return None if the list is empty

    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

# for  Example:
numbers = [10, 25, 3, 56, 88, 4,2,96]
print("Largest number:", find_largest_number(numbers))

