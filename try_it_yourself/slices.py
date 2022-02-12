# Adding cubed values in a list
cubes = [value**3 for value in range(1,11)]
# Printing the values in the cubes' list
for cube in cubes:
	print(cube)

print(f"\nThe first three items in the list are: {cubes[0:3]}.")
print(f"\nThree items from the middle of the list are: {cubes[4:7]}")
print(f"The last three items in the list are: {cubes[-3:]}")