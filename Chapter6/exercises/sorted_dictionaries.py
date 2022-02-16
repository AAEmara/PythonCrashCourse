# Adding information of the same object in a dictionary.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# Looping through a sorted dictionary.
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")