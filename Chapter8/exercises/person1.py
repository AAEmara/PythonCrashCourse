def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first':first_name, 'second':last_name}
    return person

# Function call will return a dictionary that is saved in the musician variable.
musician = build_person('jimi', 'hendrix')
print(musician)