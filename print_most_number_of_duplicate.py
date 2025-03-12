# Ask user to input a number, continue asking until the user input is invalid
given_numbers = []
while True:     # Use while loop since input is not limited
    try:
        num = int(input("Input a number: "))
        given_numbers.append(num)

# Count occurrences of each number
        number_counts = {}
        for num in given_numbers:
            if num in number_counts:
                number_counts[num] += 1
            else:
                number_counts[num] = 1

# Find the maximum count (most frequent number)
# Find all numbers with the maximum count
# Display the numbers with the most duplicates

    except ValueError:
        print("Invalid input. Exiting...")
        break