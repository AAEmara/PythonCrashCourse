# Assigning current users values in a list.
current_users = ["Aolay_11", "XxHunterxX", "boombastic",
                 "hero_Ninja", "The_DAWN"]
# Assigning new users values in a list.
new_users = ["Impossible99", "XxHunterxX", "bone_fracture",
             "hero_Ninja", "The_killer"]


# Making a lowercase copy of current users for comparison.
cp_current_users = []

for i in range(len(current_users)):
    lowercase_name = current_users[i].lower()
    cp_current_users.append(lowercase_name)


# checking new usernames.
for user in new_users:
    if user.lower() in cp_current_users:
        print("Please enter a new username!")
    else:
        print("Username is available.")