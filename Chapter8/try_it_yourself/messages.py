def show_message(txt_msgs):
    """A function that receives a text messages list 
    and print each text message"""
    for message in txt_msgs:
        print(message)

# Storing text messages values in a list.
messages = ["I love Python.", "Hello World!", "Work hard everyday!"]
# Using the function with Positional Argument.
show_message(messages)