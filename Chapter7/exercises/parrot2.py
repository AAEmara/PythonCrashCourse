# assigning a string message to propmt variable
prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

# Assigning an initial value of message variable.
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)