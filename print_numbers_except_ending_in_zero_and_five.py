# Print all the numbers starting from 0 to 100 except numbers ending in zero or ending five
exc_zero_and_five = []
for i in range(0, 101):     # For loop (to shorten the code)
    if i % 5 != 0:
        exc_zero_and_five.append(i)

print(exc_zero_and_five)