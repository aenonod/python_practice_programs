# Ask user to input 2 numbers
num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))

# If the first number is less than the second number, print the first number
if num1 < num2:
    print(f"{num1} is smaller than {num2}.")

# If the second number is less than the first number, print the second number
if num2 < num1:
    print(f"{num2} is smaller than {num1}.")