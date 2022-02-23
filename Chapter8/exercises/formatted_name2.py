# Defining a function.
# making_middle parameter optional. 
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formated."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

# Treating arguments as Positional Arguments.
# Using the function with only first_name and middle_name.
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

# Using the function with all of the three arguments.
musician = get_formatted_name('jimi', 'hendrix', 'lee')
print(musician)
