# My own favorite food 
my_foods = ["pizza", "falafel", "carrot cake"]
# Copying the previous list as my friend share the same favorite food.
friend_foods = my_foods[:]

# Adding different elements to each list name
my_foods.append("cannoli")
friend_foods.append("ice cream")

# printing the lists
print("My favorite foods are:")
for food in my_foods:
	print(food.title())

print("\nMy firend's favorite foods are:")
for food in friend_foods:
	print(food.title())