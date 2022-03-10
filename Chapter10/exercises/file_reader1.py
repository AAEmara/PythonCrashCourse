# Opening the txt file with relative file path.
with open('text_files/pi_digits.txt') as file_object:
    # Reading the file.
    contents = file_object.read()
    
# Printing the file while removing any whitespace characters
# on the right side of a string.
print(contents.rstrip())