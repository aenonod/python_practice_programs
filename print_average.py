# Ask user to input a number, continue asking until the user input is invalid
given_numbers = []
while True:     # Use while loop since input is not limited
    user_input = input("Input a number: ")
    given_numbers.append(int(user_input))

    if not user_input.isdigit():
        print("Invalid input. Exiting...")
        break

# Display the average
    if given_numbers:
        average = sum(given_numbers) / len(given_numbers)
        print("The average of the numbers is:", average)