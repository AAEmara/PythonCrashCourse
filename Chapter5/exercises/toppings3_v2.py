# Assigning values to the toppings list.
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

# Applying for loop to see the toppings added in order.
for requested_topping in requested_toppings:
    # Green peppers are sold out.
    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
    # All other toppings are available
    else:
        print(f"Adding {requested_topping}.")
    
print("\nFinished making your pizza!")