# In this python file we show how inheritance is presented in code.
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odemeter(self, mileage):
        """
        Set the odemeter reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

    def fill_gas_tank(self):
        """Filling the car's gas tank."""
        print("Please wait, We are filling the gas tank.")
        print("...")
        print("Gas tank has been filled.\nThank you!")

# Moving the attributes and methods related to battery to  a separate class
# called Battery.
class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size = 75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-KWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        # Capacity of battery is in kWh.
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315

        print(f"This car can go about {range} miles on a full charge.")

    def battery_upgrade(self):
        if self.battery_size != 100:
            self.battery_size = 100
        print(f"The car's battery has been upgraded into {self.battery_size}\
-kWh battry.")

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        """
        # Calling the __init__ method from the parent class Car.
        super().__init__(make, model, year)
        self.battery = Battery()


    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't need a gas tank!")

# Making an instance
my_tesla = ElectricCar('tesla', 'model s', 2019)
print(f"{my_tesla.get_descriptive_name()}")

my_tesla.battery.get_range()
my_tesla.battery.battery_upgrade()
my_tesla.battery.get_range()