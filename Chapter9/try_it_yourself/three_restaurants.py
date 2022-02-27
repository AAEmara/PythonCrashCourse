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

# Creating three instances of the class.
restaurant_1 = Restaurant('Sea Gull', 'Seafood')
restaurant_2 = Restaurant('Roastery coffe', 'Cafe')
restaurant_3 = Restaurant('Fresca', 'Italian')

# Creating list of restaurants' instances.
restaurants = [restaurant_1, restaurant_2, restaurant_3]

# Looping on the restaurants to use the method.
for restaurant in restaurants:
    restaurant.describe_resturant()