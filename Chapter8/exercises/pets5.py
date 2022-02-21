# Defining a function with a default parameter value.
def describe_pet(pet_name, animal_type = 'dog'):
    """Display information about a pet. """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
# Note that the order of the parameters in the function definition had to be
# changed. (Because if you wanted to use positional arguments instead of
#           keyword arguments)

# Entering the keyword arguments we need while omitting the default parameter
# value since we really consider the animal_type as a dog.
describe_pet(pet_name = "fofo") 

# function call with Positional Arguments.
describe_pet("fofo") 

# Use explicit argument values to ignore the parameter's default values.
describe_pet(pet_name = "sushi", animal_type = "cat")

# Or just positional arguments.
describe_pet("sushi", "cat")