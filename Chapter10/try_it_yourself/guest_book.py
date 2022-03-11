# This is a program that prompts the user to enter his name and records
# his entrance in a text file with each record saved in a separate line
# until the user quits the program
program_status = 'active'
filename = 'guest_book.txt'

# A while loop depending in the program's status while propmting the user for
# his entry and appending the values until the user decides to quit by pressing
# 'q' character.
while program_status == 'active':
    name = input("Please enter your first name (enter 'q' to exit): ")
    
    if name == 'q':
        program_status = 'not active'
    else:
        print(f"Hello {name.title()}, have a great day!\n")

        with open(filename, 'a') as file_object:
            file_object.write(f"{name.title()} has entered.\n")
