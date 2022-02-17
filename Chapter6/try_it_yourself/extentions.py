# This program is generalizing the formatting and insertion of any new
# information in the future.
# Saving users data in dictionary as dictionary objects.
users = {
    'aeinstien': {
        'first': 'albert',
        'last': 'einstien',
        'location': 'princeton',
        'nobel': 'yes',
        'born in': '1879',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        'nobel': 'yes',
        'born in': '1867',
        },
    }

# Looping through the dictionary.
for username, user_info in users.items():
    
    #Printing username before printing his full name.
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"

    # Printing the user's full name.
    print(f"\tFull name: {full_name.title()}")
    
    # Looping on the info of each username.
    for key, info in user_info.items():
        
        # Ignoring first and last name since we printed the full name before.
        if key == 'first' or key == 'last':
            pass
        else:
            # Printing the rest of the information as a part of generalization.
            print(f"\t{key.title()}: {info.title()}")

