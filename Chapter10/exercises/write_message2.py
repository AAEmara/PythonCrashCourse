# This program saves text to a file.
filename = 'programming2.txt'

# Opening the file in write mode 'w'.
with open(filename, 'w') as file_object:
    # You must add newline characters or the output will be squished together.
    # Adding newline characters to separate the messages.
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")