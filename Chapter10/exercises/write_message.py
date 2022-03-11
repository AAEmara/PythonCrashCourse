# This program saves text to a file.
filename = 'programming.txt'

# Opening the file in write mode 'w'.
with open(filename, 'w') as file_object:
    file_object.write("I love programming.")