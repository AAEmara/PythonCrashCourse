# Saving the input message in the group variable.
group = input("Hello, How many people are in your group? ")
group = int(group)

# Applying the conditions on the input.
if group > 8:
    print("You will have to wait for a table.")
else:
    print("The table is ready.")