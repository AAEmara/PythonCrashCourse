# This function describes the pet and its name.
def describe_pet(animal_type, pet_name):
    """Display information about a pet. """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Using the function with Keyword Arguments.
# (name-value pair arguments, where order doesn't matter)
describe_pet(pet_name ="sushi", animal_type ="cat")