# Storing values in pets list.
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

# Looping through the list to find if 'cat' value is in the list
# and remove it while its there.
while 'cat' in pets:
    pets.remove('cat')

print(pets)