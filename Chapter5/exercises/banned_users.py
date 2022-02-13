# Assigning banned users list and the user to check.
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

# Checking the user using "not in" while using IF statement.
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")