# Defining the fucntion with city and country parameters.
def city_country(city, country):
    """A function that formats the city and country entered and print it"""
    formatted_input = f"\"{city}, {country}\""

    return formatted_input.title()

# Using Propositional Arguments in the functions
print(city_country('alexandria', 'egypt'))
print(city_country('london', 'england'))
print(city_country('toronto', 'canada'))