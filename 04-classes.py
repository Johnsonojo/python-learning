# Taking into consideration MESt kitchen app, write a class to model the various objects
#  think of the real world and translate it to a class.

class User():
    first_name = ''
    last_name = ''
    email_address = ''
    phone_number = ''
    allergies = ''
    food_diet = ''
    user_type = ''
    role = ''

    def get_full_name(self):
        # return user.first_name + " " + user.last_name
        return "{},{}".format(self.first_name, self.last_name)


class MealItem():
    name = ''
    description = ''
    serving_sizes = ''
    allergens = []


class Order():
    order_details = []
    quantity = ''


# class Price():
#     pass


user = User()  # Instantiate a User class
user.first_name = "johnson"
user.last_name = "Ojo"

print(user.get_full_name())

print()
