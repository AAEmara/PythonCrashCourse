# Adding information of the same object in a dictionary.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# Looping on keys(names) only.
# Note: using favorite_languages.keys() is the same as omitting keys() method
# and using favorite_languages.
print("The following languages have been mentioned:")
for name in favorite_languages.keys():
    print(name.title())