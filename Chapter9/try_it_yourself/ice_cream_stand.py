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

# IceCreamStand class inherits from Restaurant class.
class IceCreamStand(Restaurant):
    """This class represents a specific kind of restaurants"""
    def __init__(self, restaurant_name, cuisine_type, number_served, flavors):

        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavors = flavors

# Creating an instance of IceCreamStand.
gellato = IceCreamStand("gellato", "ice cream", "40", ["mango","strawberry"])

flavor_list = gellato.flavors
print("--- Ice Cream Flavors Summary ---")
for flavor in flavor_list:
    print(f"\t{flavor.title()}")