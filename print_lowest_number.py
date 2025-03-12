# Ask user to input a number, continue asking until the user input is invalid
lowest_number = None
while True:     # Use while loop since input is not limited
    user_input = input("Input a number: ")

    if not user_input.isdigit():
        print("Invalid input. Exiting...")
        break

    number = int(user_input)

# Display the lowest number
    if lowest_number is None or number < lowest_number:
        lowest_number = number
        print("Lowest:", lowest_number)
    else:
        print("Lowest:", lowest_number)