# Ask user to input 10 numbers
odd = []
for i in range(10):     # For loop (to shorten the code)
    num = int(input(f"Input a number {i+1}: "))
    if num % 2 != 0:
        odd.append(num)

# Print how many are odd numbers
print(odd)