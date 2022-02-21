def make_shirt(size, shirt_message):
    """This function prints a sentence summarizing the size of the shirt
    and the message printed on the shirt."""
    print(f"\nShirt's size is '{size.upper()}'.")
    print(f"The message written on the shirt is '{shirt_message}'.")

# Calling the function...
# Using Positional arguments.
make_shirt('xxl', "I <3 Python")

# Calling the function...
# Using Keyword arguments.
make_shirt(shirt_message = "I <3 Python", size = "xxl")