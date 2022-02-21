# Adding the age parameter in the function beside first and last name.
def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first':first_name, 'second':last_name}
    if age:
        person['age'] = age
    return person

# Function call will return a dictionary that is saved in the musician variable.
musician = build_person('jimi', 'hendrix',27)
print(musician)