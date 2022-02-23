# Defining a function that includes an Arbitrary number of arguments.
# The asterisk in the parameter name tells python to make an empty tuple.
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

# Python packs the arguments intoa tuple even if it is a one argument.
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')