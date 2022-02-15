# Adding information of the same object in a dictionary.
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# Which language (value) does sarah (value) favours?
language = favorite_languages["sarah"].title()
print(f"Sarah's favorite language is {language}.")