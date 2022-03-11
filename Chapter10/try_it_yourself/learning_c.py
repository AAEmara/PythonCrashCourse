filename = 'learning_python.txt'
print("--- First way of printing the content ---")
# Printing the contents by reading the entire file.
with open(filename) as file_object:
    content = file_object.read()
print(content.replace('Python', 'C'))

print("\n--- Second way of printing the content ---")
# Reading the text file and printing the contents by 
# looping over the file object.
with open(filename) as file_object:
    for line in file_object:
        print(line.replace('Python', 'C').rstrip())

print("\n--- Third way of printing the content ---")
# Reading the text file and saving the contents in a list 
# then printing the contents by using a for loop on the 
# list outside the with block.
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.replace('Python', 'C').rstrip())

