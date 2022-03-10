filename = 'pi_digits.txt'
# Reading the contents of the pi_digits.txt file.
with open(filename) as file_object:
    # Reading each line and printing it through a for loop.
    for line in file_object:
        print(line.rstrip())