# Try It yourself section/ Chapter 9/ 9.12 Multiple Modules.
# Saving User class in a separate module.
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