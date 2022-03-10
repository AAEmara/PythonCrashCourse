filename = 'pi_digits.txt'

with open(filename) as file_object:
    # Saving the file contents in a list inside the with block using readline()
    # method.
    lines = file_object.readlines()

# Printing the list elements through a for loop.
for line in lines:
    print(line.rstrip())