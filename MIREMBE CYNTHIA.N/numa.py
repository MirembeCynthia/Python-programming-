def get_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers

# for Example:
numbers = [1, 2, 3, 4, 5, 6,8,10,12,14,16,18]
print("Even numbers:", get_even_numbers(numbers))