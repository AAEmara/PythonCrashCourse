# Defining a function that has a list as a parameter.
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

# Creating the list before passing it to the function.
usernames = ["sheena", "tamer", "jiji"]
greet_users(usernames)
