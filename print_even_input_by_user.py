# Ask user to input 10 numbers
even = []
for i in range(10):     # For loop (to shorten the code)
    num = int(input(f"Input number {i+1}: "))
    if num % 2 == 0:
        even.append(num)

# Print how many are even numbers
print(even)