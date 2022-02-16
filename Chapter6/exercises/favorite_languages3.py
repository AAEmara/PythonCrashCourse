# Adding information of the same favorite programming languages as a list
# in a dictionary.
favorite_languages = {
    'jen': ['python','ruby'],
    'sarah': ['c'],
    'edward': ['ruby','go'],
    'phil': ['python','haskell'],
    }

# Looping through the items of the favorite languages.
for name, languages in favorite_languages.items():
    # Checking for number of languages.
    if len(languages) > 1:
        # Printing individual's name.
        print(f"\n{name.title()}'s favorite languages are:")
    # Printing the languages.
    else :
        print(f"\n{name.title()}'s favorite language is:")
    
    # Printing language/s
    for language in languages:
        print(f"\t{language.title()}")
        