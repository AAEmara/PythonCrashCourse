filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    # Getting rid of the whitespaces on the right of the value.
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))