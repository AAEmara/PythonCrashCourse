prompt = "\nHello, Welcome to the movie theater!\nPlease enter your age "
prompt += "(Enter 'quit' to exit): "

# Initializing Flag as active variable.
active = True
while active != False:
    age = input(prompt)

    if age == 'quit':
        break
    # Checking the age conditions to determine the cost of the ticket.
    elif int(age) < 3:
        print("Your ticket is free!")
    elif int(age) >= 3 and int(age) <= 12:
        print("Your ticket price is $10.")
    elif int(age) > 12:
        print("Your ticket price is $15.")
