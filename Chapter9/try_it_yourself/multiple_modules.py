# Importing modules with aliases.
import user_module as user
import admin_module as admin

# Creating an instance of Admin class.
admin_01 = admin.Admin('connor', 'mcgregor', 33, 'ireland',
                            ['can ban user',
                            'can delete posts',
                             'can add posts']
                            )
# Testing the method used in Admin class that was inherited from Privileges
# class.
admin_01.admin.show_privileges()