# Assigning the alien information in a dictionary.
alien_0 = {'color': 'green', 'speed': 'slow'}

# Using get method to give the value of the key or a default value if the
# key doesn't exist.
# First Argumen: Dictionary's KEY, Second Argument: Default VALUE if no KEY.
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)