"""
This code reads the input from a file called input.txt and outputs the largest sum of numbers to the console. The input file should contain the numbers listed in the problem description, with one number per line and a blank line between each Elf's inventory.
"""



# Read the input
with open('/Users/tchuynh/adventofcode2022/Day1Input.txt', 'r') as f:
    lines = f.readlines()

# Keep track of the largest sum and the current sum
largest_sum = 0
current_sum = 0

# Loop over the lines in the input
for line in lines:
    # If the line is empty, we have reached the end of an Elf's inventory
    if line.strip() == '':
        # Check if the current sum is larger than the largest sum
        if current_sum > largest_sum:
            largest_sum = current_sum
        # Reset the current sum
        current_sum = 0
    else:
        # Otherwise, add the number on the line to the current sum
        current_sum += int(line.strip())

# Output the largest sum
print(largest_sum)
