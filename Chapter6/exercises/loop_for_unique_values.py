# Adding information of the same object in a dictionary.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
# Looking for unique values in the keys of the dictionary.
# Using for loop while using also set function.
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())