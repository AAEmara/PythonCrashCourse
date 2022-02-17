# Assigning information about cities and their related details.
cities = {
    "alexandria": {
        'country': 'egypt',
        'population': '5,483,605',
        'fact': 'Alexandria is the second-largest city in Egypt',
        },
    "london": {
        'country': 'england',
        'population': '9,002,488',
        'fact': 'London is the smallest city in England',
        },
    "paris": {
        'country': 'france',
        'population': '2,165,423',
        'fact': 'the Louvre is the world’s biggest art museum'
        },
    }

# Looping through the information about each city.
for city, information in cities.items():
    print(f"\nDid you know that the city of {city.title()}:")
    print(f"\tIs in {information['country'].title()} and its population"
        f" is {information['population']}.")
    print(f"\tA fun fact that {information['fact']}.")