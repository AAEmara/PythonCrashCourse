# Assigning users to users list.
users_list = ["abdelrahman", "samak", "admin", "eissa", "rehab"]

# The for loop to greet each user.
for user in users_list:
    # Special condition for the "admin".
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again.")