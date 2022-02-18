# assigning a string message to propmt variable
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

# This time we use the flag concept to determine the status of the program.
# We save the status in a variable called active.
active = True

while active:
    message = input(prompt)

    # The condition to close the program.
    if message == 'quit':
        active = False

    # Keeps the program running.
    else:
        print(message)