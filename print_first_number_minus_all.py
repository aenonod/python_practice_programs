# Ask user to input 10 numbers
given_numbers = []
for i in range(10):     # For loop (to shorten the code)
    num = int(input(f"Input number {i+1}: "))
    given_numbers.append(num)

# Print the result of the first number minus all of the remaining numbers
result = given_numbers[0] - sum(given_numbers[1:])
print("The result is:", result)