

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
