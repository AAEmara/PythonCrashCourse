def send_messages(txt_msgs, sent_messages):
    """A function that print each text message 
    and moves each message to a new list"""
    while txt_msgs:
        # Popping values from the list in order.
        message = txt_msgs.pop()
        print(message)
        sent_messages.append(message)


# Storing text messages values in a list.
messages = ["I love Python.", "Hello World!", "Work hard everyday!"]
# Empty list.
finished_messages = []
# Using the function with Positional Argument.
send_messages(messages, finished_messages)

# Checking on both lists.
# Original list.
print(messages)
# Copied list
print(finished_messages)