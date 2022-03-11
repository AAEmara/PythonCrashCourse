# This program saves text to a file.
filename = 'programming3.txt'

# Opening the file in write mode 'w'.
with open(filename, 'a') as file_object:
    # You must add newline characters or the output will be squished together.
    # Adding newline characters to separate the messages.
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")