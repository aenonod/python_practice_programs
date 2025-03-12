# Ask user to input 10 numbers
given_numbers = []
for i in range(10):     # For loop (to shorten the code)
    num = int(input(f"Input number {i+1}: "))
    given_numbers.append(num)

# Use class set for easier tracking of numbers that have already been displayed
seen = set()
with_duplicate = []

# Display all numbers that have duplicate
for num in given_numbers:
    if given_numbers.count(num) != 1 and num not in seen:
        with_duplicate.append(num)
        seen.add(num)

print("Numbers with duplicate:", with_duplicate)