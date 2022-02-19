# Saving the prompt message in a variable.
opener = "\nIf there is only one place you would like to visit in this world,"
opener += "\nWhere would you go? "

responses = {}

polling_active = True

while polling_active == True:
    print(opener)

    username_prompt = input("\nEnter your username: ")
    place_prompt = input("Enter the place you would like to visit: ")

    responses[username_prompt] = place_prompt
    # Exit the program ?
    exit = input("Exit the program? (yes/no):")
    if exit == 'yes':
        polling_active = False


print("\n--- Polling Results ---")
i = 0
for username, response in responses.items():
    i += 1
    print(f"{i}-) {username.title()}: {response.title()}")