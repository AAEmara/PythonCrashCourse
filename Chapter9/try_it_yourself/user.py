class User:
    """A class that represents a user."""

    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country

    def describe_user(self):
        print("\n--- User Information ---")
        information = {'first name' : self.first_name,
                        'last name' : self.last_name,
                        'age' : self.age,
                        'country' : self.country,
                        }
        for key, info in information.items():
            print(f"-{key.title()} : {str(info).title()}")

    def greet_user(self):
        name = f"{self.first_name} {self.last_name}"
        print(f"\nHello {name.title()}, Have a nice day!")

# Creating instances of User class.
user_1 = User('abdelrahman', 'emara', 24, 'egypt')
user_2 = User('jhon', 'wick', 99, 'united states of america')

# Calling class methods.
user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()