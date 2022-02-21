# Defining the function with two parameters and one of them is with
# a default value.
def describe_city(city, country = "Egypt"):
    """A function that prints the city name and in which country."""
    print(f"\n{city.title()} is in {country.title()}.")

# Calling the function three times one of them without default values.
# 1st function call.
describe_city(city = 'alexandria')
# 2nd function call.
describe_city(city = 'cairo')
# 3rd function call.
describe_city(city = 'london', country = 'england')