# Assigning each of my friends' favorite number in a dictionary.
fav_nums = {
    'jhon': [7, 1],
    'michael': [9, 5],
    'todd': [5, 3],
    'ronald': [2, 7, 9],
    'vlad': [10],
    }
    
# Looping through the dictionary to print friends' names and their
# favorite numbers.
for name, numbers_list in fav_nums.items():
    if len(numbers_list) > 1:
        # Taking multiple numbers into consideration.
        print(f"\n{name.title()}'s favorite numbers are:")
        # Printing numbers
        for number in numbers_list:
            print(f"\t{number}")
    else:
        # Taking a single number into consideration.
        print(f"\n{name.title()}'s favorite number is:")
        # Printing the single number.
        for number in numbers_list:
            print(f"\t{number}")

