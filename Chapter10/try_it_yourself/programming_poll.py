# This is a program that prompts the user to enter his name and records
# his entrance in a text file with each record saved in a separate line
# until the user quits the program
program_status = 'active'
filename = 'programming_poll.txt'

# A while loop depending in the program's status while propmting the user for
# his entry and appending the values until the user decides to quit by pressing
# 'q' character.
while program_status == 'active':
    answer = input("Why you like programming ? (enter 'q' to exit): ")
    
    if answer == 'q':
        program_status = 'not active'
    else:
        # Appendnig the answers by using the write method.
        with open(filename, 'a') as file_object:
            file_object.write(f"{answer}\n")
