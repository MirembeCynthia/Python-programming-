def multiplication_table(number):
    for i in range(1, 13):
        print(f"{number} x {i} = {number * i}")

# Example usage:
num = int(input("Enter a number: "))
multiplication_table(num)
