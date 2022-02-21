# Defining a greeting function responsible for greeting the user!
# The user must enter his username inside the parentheses.
def greet_user(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is a infinite loop!
while True:
    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Second name: ")

    formatted_name = greet_user(f_name, l_name)
    print(f"\nHello, {formatted_name}!")