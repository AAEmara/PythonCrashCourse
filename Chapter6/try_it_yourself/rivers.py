# Assigning the major three rivers in a dictionary.
top_rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
    }
# Looping through key-value pairs to print sentences.
for river, country in top_rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

# Printing the name of each river in the dictionary.
for river in top_rivers.keys():
    print(river.title())
for country in top_rivers.values():
    print(country.title())