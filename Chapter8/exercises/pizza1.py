# Defining a function that includes an arbitrary number of arguments.
# The asterisk in the parameter name tells python to make an empty tuple.
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print(toppings)

# Python packs the arguments intoa tuple even if it is a one argument.
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')