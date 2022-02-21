# Defining a function.
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formated."""

    full_name = f"{first_name} {last_name}"
    return full_name.title()

# Saving the formatted name in a variable then printing it.
musician = get_formatted_name('jimi', 'hendrix')
print(musician)