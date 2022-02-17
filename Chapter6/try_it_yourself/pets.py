# Assigning pets and their owners in dictionaries
pet_0 = {'kind': 'dog', 'owner': 'fatma',}
pet_1 = {'kind': 'cat', 'owner': 'rehab',}
pet_2 = {'kind': 'cat', 'owner': 'omar',}

# Storing dictionaries in a list.
pets = [pet_0, pet_1, pet_2]

# Looping through the list for printing information.
for pet in pets:
    print(f"{pet['owner'].title()} owns a {pet['kind']}.\n")