# Print all the numbers starting from 0 to 100 except numbers ending in zero
exc_zero = []
for i in range(0, 101):     # For loop (to shorten the code)
    if i % 10 != 0:
        exc_zero.append(i)

print(exc_zero)