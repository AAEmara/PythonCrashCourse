filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    # Removing any whitespaces by using strip() method.
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))