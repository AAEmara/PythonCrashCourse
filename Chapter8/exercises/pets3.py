# This function describes the pet and its name.
def describe_pet(animal_type, pet_name):
    """Display information about a pet. """
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Using the function with Positional Arguments. (providing arguments in order.)
# If you entered the arguments in wrong order this will give you a funny output.
describe_pet("sushi", "cat")