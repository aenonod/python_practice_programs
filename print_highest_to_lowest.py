# Ask user to input a number, continue asking until the user input is invalid
given_numbers = []
while True:     # While loop (keep asking the user for input until invalid input is entered)
    user_input = input("Input a number: ")

    if not user_input.isdigit():
        print("Invalid input. Exiting...")
        break

    number = int(user_input)
    given_numbers.append(number) 

# # Display the number from highest to lowest using sort() function
    given_numbers.sort(reverse=True)
    print(given_numbers)