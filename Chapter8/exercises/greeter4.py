# Defining a greeting function responsible for greeting the user!
# The user must enter his username inside the parentheses.
def greet_user(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# This is an infinite loop!
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    # Prompting the user to either quit or enter first name.
    f_name = input("First name: ")
    if f_name == 'q':
        break

    # Prompting the user to either quit or enter last name.
    l_name = input("Second name: ")
    if l_name == 'q':
        break  

    formatted_name = greet_user(f_name, l_name)
    # Greeting the user as a final output!
    print(f"\nHello, {formatted_name}!")