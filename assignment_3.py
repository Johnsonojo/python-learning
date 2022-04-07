# Assignment 03
# Taking into consideration MESt kitchen app, write a class to model the various objects:
# think of the real world and translate it to a class.

# A user class


class User():
    first_name = ''
    last_name = ''
    email_address = ''
    phone_number = ''
    gender = ''
    allergies = ''
    user_type = ''

    def __init__(self, first_name, last_name, email_address, phone_number, gender, allergies, user_type):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.phone_number = phone_number
        self.gender = gender
        self.allergies = allergies
        self.user_type = user_type


# A meal item class
class MealItem():
    meal_name = ''
    meal_description = ''
    serving_sizes = ''
    meal_image = ''

    def __init__(self, meal_name, meal_description, serving_sizes, meal_image):
        self.meal_name = meal_name
        self.meal_description = meal_description
        self.serving_sizes = serving_sizes
        self.meal_image = meal_image


# An order class
class Order():
    order_details = ''
    quantity = ''

    def __init__(self, order_details, quantity):
        self.order_details = order_details
        self.quantity = quantity


# Instantiate a user as an EIT
user_as_eit = User('Johnson', 'Ojo', 'johnson@ojo.com',
                   '+23435684521', 'male', 'none', 'EIT')

# Instantiate a user as an Staff
user_as_staff = User('Linda', 'Mensa', 'linda@mensa.com',
                     '+23435684567', 'female', 'none', 'STAFF')


# Instantiate a meal object
new_meal = MealItem('Beans and plantain with grilled chicken',
                    'This is the regular stew been with fried plantain and grillled chicken', '1 plate', '')


# Instantiate an order object
new_order = Order('Beans and plantain with grilled chicken', 1)


print(user_as_staff.last_name)
print(user_as_eit.first_name)
print(new_meal.meal_name)
print(new_order.quantity)
