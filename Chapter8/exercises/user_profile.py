# Defining a function that accepts keyword arguments which asks python to
# create a dictionary and saves whatever keyword arguments are passed to the
# function into the dictionary.
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                            location = 'princeton', 
                            field = 'physics'
                            )
print(user_profile)