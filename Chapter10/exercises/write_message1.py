# This program saves text to a file.
filename = 'programming1.txt'

# Opening the file in write mode 'w'.
with open(filename, 'w') as file_object:
    # You must add newline characters or the output will be squished together.
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")