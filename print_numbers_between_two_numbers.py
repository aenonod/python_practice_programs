# Ask user to input 2 numbers
num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))

# Make sure that the second number is larger than the first one
if num1 > num2:
    num1, num2 = num2, num1

# Print all the numbers between the two numbers
if num2 - num1 > 1:
    print(f"Numbers in the middle of {num1} and {num2}: ")
    for num in range(num1 + 1, num2):
        print(num, end=' ')
else:
    print("There are no numbers in the middle.")