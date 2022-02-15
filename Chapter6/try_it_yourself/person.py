# Assigning the information related to my friend.
my_friend = {
    'first_name': 'abdelrahman',
    'last_name': 'eissa',
    'city': 'alexandria',
    }
# Assigning each info in a variable
first_name = my_friend['first_name'].title()
last_name = my_friend['last_name'].title()
city = my_friend['city'].title()

# Printing the information of my friend.
print(f"My friends' name is {first_name} {last_name}.")
print(f"He lives in {city}.")