# Assinging an empty list to users list.
users_list = []

# The for loop to greet each user.
# Checking that the list is not empty.
if users_list:
    for user in users_list:
        # Special condition for the "admin".
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again.")
else:
    # The message if the if condition was FALSE.
    print("We need to find some users!")