# Assigning age variable with its value.
age = 12

# Setting the if-elif chain.
if age < 4:
    price = 0
elif age >= 4 and age < 18:
    price = 25
# Adding the seniors in our conditional if-elif.
elif age < 65:
    price = 40
# There is no need for an else statement when there is a chance to use
# an elif statement to catch the condition. 
elif age >= 65:
    price = 20
# If you wanted to change the message you would only apply the change to
# the print statement.
print(f"Your admission price is ${price}.")