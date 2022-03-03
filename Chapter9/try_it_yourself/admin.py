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

# Creating Admin class that inherits from User class.
class Admin(User):
    """An admin is a special type of users."""

    def __init__(self, first_name, last_name, age, country, privileges):

        super().__init__(first_name, last_name, age, country)
        self.privileges = privileges

    def show_privileges(self):
        """Showing the privileges of an admin."""
        print("--- Admin Privileges ---")
        for privilege in self.privileges:
            print(f"{privilege.title()}.")

# Creating an instance of the class and using its method.
admin_00 = Admin('jhon', 'wick', '55', 'usa',
                ['Can delete post', 'Can ban user', 'Can add post'])
admin_00.show_privileges()
