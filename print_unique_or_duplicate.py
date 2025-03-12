# Ask user to input a number, continue asking until the user input is invalid
given_numbers = []
while True:     # Use while loop since input is not limited
    num = input("Input a number: ")

# Check if the user input is a digit
    if not num.isdigit():
        print("Invalid input. Exiting...")
        break

# Display "Unique" after input when the inputted number don't have duplicate
    if num not in given_numbers:
        print("Unique")
        given_numbers.append(num)

# Display "Duplicate" after input when the inputted number have duplicate
    else:
        print("Duplicate")