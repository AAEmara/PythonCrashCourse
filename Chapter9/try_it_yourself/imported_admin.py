# Importing the privileges_module while using an alias.
import privileges_module as privilege

# Creating an instance of Admin class.
admin_01 = privilege.Admin('connor', 'mcgregor', 33, 'ireland',
                            ['can ban user',
                            'can delete posts',
                             'can add posts']
                            )
# Testing the method used in Admin class that was inherited from Privileges
# class.
admin_01.privileges.show_privileges()