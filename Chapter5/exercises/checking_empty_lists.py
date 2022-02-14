# Declaring an empty list.
requested_toppings = []

# If statement when used with lists in python, it returns TRUE if the list
# contains at least of one item, and returns FALSE if the list is empty.  
if requested_toppings:
    # Applying for loop to see the toppings added in order.
    for requested_topping in requested_toppings:
        
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")

else:
    print("Are you sure you want a plain pizza?")