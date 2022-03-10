filename = 'pi_million_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    # Removing any whitespaces by using strip() method.
    pi_string += line.strip()
    
# Showing first 50 decimal places from the pi millio digits
print(f"{pi_string[:52]}...")
print(len(pi_string))