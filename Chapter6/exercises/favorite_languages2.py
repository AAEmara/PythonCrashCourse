# Adding information of the same object in a dictionary.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# Looping through the dictionary.
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")