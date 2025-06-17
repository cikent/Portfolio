# Declare initial Integer variable with a value of 0
total = 0
# Create a For Loop to iterate through each of the values in a defined range
for num in range(101):
    # For each value in the range, add it to the combined values
    total = total + num
    # Print to console the present number and the present Subtotal
    print(f'Current number in range: {num}\nCurrent Subtotal: {total}\n')
# Print the collective total after iterating through the entire range
print(f'The complete Total is: {total}')
