# Ask user to input a number, continue asking until the user input is invalid
highest_number = None
while True:     # Use while loop since input is not limited
    user_input = input("Input a number: ")

    if not user_input.isdigit():
        print("Invalid input. Exiting...")
        break

    number = int(user_input)

# Display the highest 
    if highest_number is None or number > highest_number:
        highest_number = number
        print("Highest:", highest_number)
    else:
        print("Highest:", highest_number)