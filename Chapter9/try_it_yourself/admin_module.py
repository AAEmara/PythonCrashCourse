# Try It yourself section/ Chapter 9/ 9.12 Multiple Modules.
# Saving Privileges and Admin classes in a separate module.
from user_module import User

class Privileges:
    def __init__(self, privileges):

        self.privileges = privileges

    def show_privileges(self):
        """Showing the privileges of an admin."""
        print("--- Admin Privileges ---")
        for privilege in self.privileges:
            print(f"{privilege.title()}.")

class Admin(User):
    """An admin is a special type of users."""

    def __init__(self, first_name, last_name, age, country, privileges):

        super().__init__(first_name, last_name, age, country)
        self.privileges = Privileges(privileges)