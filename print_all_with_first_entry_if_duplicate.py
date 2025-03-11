# Ask user to input 10 numbers
given_numbers = []
for i in range(10):
    num = int(input(f"Input number {i+1}: "))
    given_numbers.append(num)

# Use class set for easier tracking of numbers that have already been displayed
seen = set()

# Display all numbers
# For numbers with duplicate, display only the first entry
for num in given_numbers:
    if num not in seen:
        print(num, end=', ')
        seen.add(num)