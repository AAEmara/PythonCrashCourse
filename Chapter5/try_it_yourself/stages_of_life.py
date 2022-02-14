# Assigning the age value of a person.
age = 24
# Using the if-elif-else chain in determining the person's stage of life.
if age < 2:
    print("The person is a baby.")
elif age >= 4 and age < 13:
    print("The person is a toddler.")
elif age >= 13 and age < 20:
    print("The person is a teenager.")
elif age >= 20 and age < 65:
    print("The person is an adult.")
else:
    # 65 years or older
    print("The person is an elder.")