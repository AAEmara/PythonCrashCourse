class User:
    """A class that represents a user."""

    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login_attempts = 0

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

    def increment_login_attempts(self):
        """Increments the value of login_attempts attribute by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the value of login_attempts attribute to be equal to zero."""
        self.login_attempts = 0


# Creating instances of User class.
user_1 = User('abdelrahman', 'emara', 24, 'egypt')

# Calling the increment_login_attempts method several times.
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()

# Checking that the values of login_attempts attribute was effectively changed.
username_1 = f"{user_1.first_name} {user_1.last_name}"
print (f"{username_1.title()} has attempted to login {user_1.login_attempts} times")
user_2 = User('jhon', 'wick', 99, 'united states of america')

# Resetting the login attempts.
user_1.reset_login_attempts()
print (f"{username_1.title()} has attempted to login {user_1.login_attempts} times")