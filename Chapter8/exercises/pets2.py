# This function describes the pet and its name.
def describe_pet(animal_type, pet_name):
    """Display information about a pet. """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Using multiple function calls with Positional Arguments.
# (providing arguments in order.)
describe_pet("cat", "sushi")
describe_pet("dog", "fofo")