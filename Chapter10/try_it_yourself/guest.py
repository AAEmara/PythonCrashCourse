# This program prompts the user to enter their first name and then saves it
# in a txt file.
filename = 'user_names.txt'
name = input("Please enter your first name: ")

with open(filename, 'a') as file_object:
    file_object.write(f"{name}\n")