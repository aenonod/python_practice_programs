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
        max_count = 0
        for count in number_counts.values():
            if count > max_count:
                max_count = count

# Find all numbers with the maximum count
        most_duplicate = []
        for num, count in number_counts.items():
            if count == max_count:
                most_duplicate.append(num)

# Display the numbers with the most duplicates
        print("Number/s with the most duplicates:", most_duplicate)

    except ValueError:
        print("Invalid input. Exiting...")
        break