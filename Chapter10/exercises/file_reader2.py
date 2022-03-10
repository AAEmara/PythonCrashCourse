# Opening the txt file with absolute file path.
# Saving the file path in a variable.
file_path = '/trial/python_txt_files/pi_digits.txt'
with open(file_path) as file_object:
    # Reading the file.
    contents = file_object.read()
    
# Printing the file while removing any whitespace characters
# on the right side of a string.
print(contents.rstrip())