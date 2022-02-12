# Creating an empty list to add values inside it later
cubes = []

# Using a for loop to cube values in range of 1~10
for value in range(1,11):
	cube = value**3
	cubes.append(cube**3)
	# Printing the cube of the value
	print(cube)