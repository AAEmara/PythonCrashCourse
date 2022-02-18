toppings = "\nHello, Please enter the toppings you would like to add "
toppings += "\non your pizza (Enter 'quit' to exit ordering): "

# Intial status in variable ordering.
ordering = True

# The program runs while ordering status is TRUE.
while ordering:
    message = input(toppings)
    
    # A condition where if the input was equal quit the value of ordering value
    # will be false and the program quits.
    if message == "quit":
        ordering = False
    else:
        print(f"\nWe are adding {message} on your pizza!")
