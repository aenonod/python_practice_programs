# Ask user to input 2 numbers
num1 = float(input("Input first number: "))
num2 = float(input("Input second number: "))

# Print the quotient of the two numbers with the decimal point
if num2 != 0:
    print("The quotient is:", num1 / num2)

# State that division by zero is not allowed
else:
    print("Division by zero is not allowed.")
