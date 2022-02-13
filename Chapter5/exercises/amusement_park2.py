# Assigning age variable with its value.
age = 12

# Setting the if-elif-else chain.
# It is a more simple way to help you change the code in the future.
if age < 4:
    price = 0
elif age >= 4 and age < 18:
    price = 25
else:
    price = 40
# If you wanted to change the message you would only apply the change to
# the print statement.
print(f"Your admission price is ${price}.")