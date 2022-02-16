# Adding information of the same object in a dictionary.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# Making a list of people that should take the poll.
people = ['amal', 'sabrin', 'jen', 'nehad', 'sarah']
# Thanking individuals for taking the poll and inviting who didn't.
for person in people:
    if person in favorite_languages.keys():
        print(f"Thank you {person.title()} for taking the poll!")
    else:
        print(f"Hey {person.title()}, we invite you to take the poll.")