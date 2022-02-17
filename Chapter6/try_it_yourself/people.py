# Assigning the information related to my friends.
my_friend_0 = {
    'first_name': 'abdelrahman',
    'last_name': 'eissa',
    'city': 'alexandria',
    }
my_friend_1 = {
    'first_name': 'amr',
    'last_name': 'hesham',
    'city': 'alexandria',
    }

my_friend_2 = {
    'first_name': 'amr',
    'last_name': 'shaher',
    'city': 'cairo',
    }
# Saving my friends in people list.
people = [my_friend_0, my_friend_1, my_friend_2]

# Looping through the people and printing their information.
for friend in people:
    name = f"{friend['first_name']} {friend['last_name']}"
    print(f"My friend's name is {name.title()}.")
    print(f"He lives in {friend['city'].title()}.\n")
