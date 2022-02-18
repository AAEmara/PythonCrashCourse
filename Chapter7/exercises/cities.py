# Saving the message in prompt variable.
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)

    if city == 'quit':
        # Breaking the program if the the user entered 'quit'.
        break
    else:
        print(f"I'd love to go to {message.title()}!")