# Assigning known programming words in a dictionary.
programming_words = {
    'print': 'a function that gives a representation of the output needed\
 in the terminal.',
    'range': 'a function gives a set of numbers when given the start,\
 end and step',
    'if': 'a conditional statement that checks a condition and takes an action\
 if the condition is achieved.',
    'for': 'a loop statement that iterates over a set of elements',
    'list': 'a function that creates a list',
    '.strip()': 'a method that removes whitespaces from both sides of the value',
    '.lstrip()': 'a method that removes whitespaces from the left side\
 of the value',
    '.rstrip()': 'a method that removes whitespaces from the right side\
 of the value',
    '.items()': 'a method used in dictionaries to give the key and the value in\
 \n          a for loop',
    '.values()': 'a method used in dictionaries to give just the values\
 in a for loop',
    }

# Looping through the dictionary key-value pairs.
for word, meaning in programming_words.items():
   print(f"\n{word}: {meaning}.")