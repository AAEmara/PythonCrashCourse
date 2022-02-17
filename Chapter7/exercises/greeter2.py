# saving the message in a variable and passing it later on to the print
# statment.
prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
# Appling the input function on the propmt variable that contains the message.
name = input(prompt)
print(f"\nHello, {name}!")