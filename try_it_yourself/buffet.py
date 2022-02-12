# Declaring a tuple variable saving simple foods in a resturant.
basic_foods = ("fries", "beans", "biscuts", "cheese", "salad")

# Performing a for loop on the tuple to print the basic food.
for food in basic_foods:
	print(food.title())

# This commented assigned tuple item will lead to an error.
# Remove the comment to see what error appears!
#basic_foods[2] = "falafel"
print("\n")
# Changing the restaurant menu by changing two of its items.
basic_foods = ("fries", "falafel", "pie", "cheese", "salad")
# Printing new menue using a for loop on the new tuple.
for food in basic_foods:
	print(food.title())