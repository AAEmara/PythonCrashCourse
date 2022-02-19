responses = {}

# Setting up a Flag to indicate that the program is running
polling_active = True

while polling_active == True:

    # Prompting the user to enter his/her name and response.
    name = input("\nPlease enter your name: ")
    response = input("Which mountain would you like to climb someday? ")

    # Assigning the response (value) to the name of the user(key).
    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")