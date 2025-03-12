# Ask user to input 10 numbers
given_numbers = []
for i in range(10):     # For loop (to shorten the code)
    num = int(input(f"Input number {i+1}: "))
    given_numbers.append(num)

# Display all numbers that don't have duplicate
unique_numbers = []
for num in given_numbers:
    if given_numbers.count(num) == 1:
        unique_numbers.append(num)

print("Numbers without duplicate:", unique_numbers)