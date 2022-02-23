def car_profile(manufacturer, model_name, **car_info):
    """Stores a car info into a dictionary and returns it back"""
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name

    return car_info

# Saving the function output in a variable.
car_0 = car_profile('toyota', 'avalon trd 2022',
            made_in = 'japan', body_type = 'sedan',
            no_of_cylinders = '6', gear_box = '8-speed')
# Printing the output.
print(car_0)