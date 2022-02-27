class Restaurant:
    """A class that represents a restaurant."""

    def __init__(self, restaurant_name, cuisine_type, number_served):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_resturant(self):
        print(f"\nThe restaurant's name is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print("\nThe restaurant is open.")

    def set_number_served(self, number_served):
        self.number_served = number_served


# Creating an instance of the class.
restaurant = Restaurant('Sea Gull', 'Seafood', 47)

# Using class attributes.
print(f"The restaurant has served {restaurant.number_served} people.")

# Changing the value of the number_surved attribute then printing it again.
restaurant.number_served = 50
print(f"The restaurant has served {restaurant.number_served} people.")

# Calling class methods.
restaurant.set_number_served(57)
print(f"The restaurant has served {restaurant.number_served} people.")
