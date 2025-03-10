# Ask user to input 10 numbers
sum = 0
for i in range(10):     # For loop (to shorten the code)
    num = int(input(f"Input a number {i+1}: "))
    sum += num

# Print the sum of all the numbers
print("The sum is:", sum)
