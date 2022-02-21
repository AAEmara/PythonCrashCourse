def make_shirt(size = 'l', shirt_message = 'I Love Python'):
    """This function prints a sentence summarizing the size of the shirt
    with a default large size and the message printed on the shirt
    defaulted to 'I Love Python'."""
    print(f"\nShirt's size is '{size.upper()}'.")
    print(f"The message written on the shirt is '{shirt_message}'.")

# A large sized shirt with default message.
make_shirt()
# A medium sized shirt with default message.
make_shirt(size = 'm')
# A shirt of any size with different message.
make_shirt(size = 'XXL', shirt_message = 'I <3 Python')