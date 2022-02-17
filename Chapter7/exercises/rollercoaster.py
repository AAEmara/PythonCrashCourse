# Assigning the input function message in height variable.
height = input("How tall are you, in inches? ")
# Converting the input into an integer datatype.
height = int(height)

# Checking on conditions with the numerical values before printing the output.
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")