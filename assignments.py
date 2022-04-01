# Assignment 01
# write a python code that store the foolowing
# Employee Id
# First name
# Last Name
# Basic Salary
# Allowance
# Pension Scheme
# Tax
# Net Salary =((Basic Salary-Tax-Penseion Scheme) + Allowance)
# Print each variable


def calculateBasicSalary():
    Employee_Id = 6798065
    First_Name = "Johnson"
    Last_Name = "Ojo"
    Basic_Salary = 200000
    Allowance = 5000
    Pension_Scheme = 1000
    Tax = (5 / 100) * Basic_Salary
    Net_Salary = ((Basic_Salary - Tax - Pension_Scheme) + Allowance)
    print(
        f'Employee {First_Name} {Last_Name} with id number {Employee_Id} has a monthly basic salary of {Net_Salary} USD')


calculateBasicSalary()

# Assignment 02
#  Create a list of 10 users to add the following fields
# Id
# Name
# Email
# Phone Number
# Number of visits
# Posts:
#    - Post Id,
#    - Title,
#    - Summary

# Write a for loop to iterate through the list of users and print
# user = lackey
# print(number of visits)
# Print(number of posts)

users = [
    {
        "id": 1,
        "name": "John Smith",
        "email": "john@smith.com",
        "phone_number": "08032545611",
        "number_of_visits": 11,
        "number_of_posts": 2,
        "posts": [
            {
                "id": 1,
                "title": "sunt aut facere repellat reprehenderit",
                "summary": "This is summary 1"
            },
            {
                "id": 2,
                "title": "ea molestias quasi  qui ipsa sit aut",
                "summary": "This is summary 2"
            },
        ]
    },
    {
        "id": 2,
        "name": "James Smith",
        "email": "james@smith.com",
        "phone_number": "08032545612",
        "number_of_visits": 12,
        "number_of_posts": 2,
        "posts": [
            {
                "id": 1,
                "title": "eum et est occaecati",
                "summary": "This is summary 3"
            },
            {
                "id": 2,
                "title": "nesciunt quas odio",
                "summary": "This is summary 4"
            },
        ]
    },
    {
        "id": 3,
        "name": "Jude Smith",
        "email": "jude@smith.com",
        "phone_number": "08032545613",
        "number_of_visits": 13,
        "number_of_posts": 2,
        "posts": [
            {
                "id": 1,
                "title": "magnam facilis autem",
                "summary": "This is summary 5"
            },
            {
                "id": 2,
                "title": "dolorem dolore est ipsam",
                "summary": "This is summary 6"
            },
        ]
    },
    {
        "id": 4,
        "name": "Joy Smith",
        "email": "joy@smith.com",
        "phone_number": "08032545614",
        "number_of_visits": 14,
        "number_of_posts": 2,
        "posts": [
            {
                "id": 1,
                "title": "optio molestias id quia eum",
                "summary": "This is summary 7"
            },
            {
                "id": 2,
                "title": "et ea vero quia laudantium autem",
                "summary": "This is summary 8"
            },
        ]
    },
    {
        "id": 5,
        "name": "Jane Smith",
        "email": "jane@smith.com",
        "phone_number": "08032555615",
        "number_of_visits": 15,
        "number_of_posts": 2,
        "posts": [
            {
                "id": 1,
                "title": "in quibusdam tempore odit est dolorem",
                "summary": "This is summary 9"
            },
            {
                "id": 2,
                "title": "voluptatem eligendi optio",
                "summary": "This is summary 10"
            },
        ]
    },
    {
        "id": 6,
        "name": "Jax Smith",
        "email": "jax@smith.com",
        "phone_number": "08032555616",
        "number_of_visits": 16,
        "number_of_posts": 2,
        "posts": [
            {
                "id": 1,
                "title": "eveniet quod temporibus",
                "summary": "This is summary 11"
            },
            {
                "id": 2,
                "title": "adipisci placeat illum aut reiciendis qui",
                "summary": "This is summary 12"
            },
        ]
    },
    {
        "id": 7,
        "name": "Jill Smith",
        "email": "jill@smith.com",
        "phone_number": "08032555617",
        "number_of_visits": 17,
        "number_of_posts": 2,
        "posts": [
            {
                "id": 1,
                "title": "in quibusdam tempore odit est dolorem",
                "summary": "This is summary 13"
            },
            {
                "id": 2,
                "title": "doloribus ad provident suscipit at",
                "summary": "This is summary 14"
            },
        ]
    },
    {
        "id": 8,
        "name": "Jayden Smith",
        "email": "jayden@smith.com",
        "phone_number": "08032555618",
        "number_of_visits": 18,
        "number_of_posts": 2,
        "posts": [
            {
                "id": 1,
                "title": "maxime id vitae nihil numquam",
                "summary": "This is summary 15"
            },
            {
                "id": 2,
                "title": "rem alias distinctio quo quis",
                "summary": "This is summary 16"
            },
        ]
    },
    {
        "id": 9,
        "name": "Juliet Smith",
        "email": "juliet@smith.com",
        "phone_number": "09032555619",
        "number_of_visits": 19,
        "number_of_posts": 2,
        "posts": [
            {
                "id": 1,
                "title": "quasi id et eos tenetur aut quo autem",
                "summary": "This is summary 17"
            },
            {
                "id": 2,
                "title": "iusto eius quod necessitatibus culpa ea",
                "summary": "This is summary 18"
            },
        ]
    },
    {
        "id": 10,
        "name": "Justina Smith",
        "email": "justina@smith.com",
        "phone_number": "09032555620",
        "number_of_visits": 20,
        "number_of_posts": 2,
        "posts": [
            {
                "id": 1,
                "title": "doloremque illum aliquid sunt",
                "summary": "This is summary 19"
            },
            {
                "id": 2,
                "title": "qui explicabo molestiae dolorem",
                "summary": "This is summary 20"
            },
        ]
    },
]

for user in users:
    print(
        {
            "author": user["name"],
            "number_of_posts": user["number_of_posts"],
            "number_of_visits": user["number_of_visits"]
        }
    )
    # print(user["name"])
    # print(user["number_of_posts"])
    # print(user["number_of_visits"])

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
