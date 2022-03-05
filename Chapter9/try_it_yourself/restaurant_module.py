class Restaurant:
    """A class that represents a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"\nThe restaurant's name is {self.restaurant_name}.")
        print(f"The cuisine type is {self.cuisine_type}.")

    def open_restaurant(self):
        print("\nThe restaurant is open.")