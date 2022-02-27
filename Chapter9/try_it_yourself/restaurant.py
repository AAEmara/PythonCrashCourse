class Restaurant:
    """A class that represents a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_resturant(self):
        print(f"\nThe restaurant's name is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print("\nThe restaurant is open.")

# Creating an instance of the class.
restaurant = Restaurant('Sea Gull', 'Seafood')

# Using class attributes.
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Calling class methods.
restaurant.describe_resturant()
restaurant.open_restaurant()
