# if Statement
# age =18

# if age < 18:
#     print("You're still growing")
# elif age >= 18 and age < 21:
#     print("You are an adolescent")
# else:
#     print("You're an adult")
    
# for loop
# users = ["Johnson", "James", "Jude", "Justina", "Joshua", "Jesus"]

# for user in users:
#     print(user)

# while loop
# users = ["Johnson", "James", "Jude", "Justina", "Joshua", "Jesus"]

# num =10
# stepper=0

# while(stepper <= num):
#     print(stepper)
#     stepper +=1
    
    
# users = ["Johnson", "James", "Jude", "Justina", "Joshua", "Jesus"]
# num = len(users)
# stepper=0

# while(stepper < num):
#     print(users[stepper])
#     stepper +=1
    



# num =100    
# numbs =range(num)
# sum=0

# for numb in numbs:
#     sum += numbs[numb]
# print(sum)

# # or
# print(num*(num +1 )/2 -num)

# Assignment
# build a calculator

def calculate(num1,num2, operator):
    if operator == '+':
        print(num1 + num2)
    elif operator == '-':
        print(num1 - num2)
    elif operator == '*':
        print(num1 * num2)
    elif operator == '/':
        print(num1 / num2)
    elif operator == '%':
        print(num1 % num2)
    else: print("incorrect operator")
    
calculate(10,2,"+")
calculate(10,2,"-")
calculate(10,2,"*")
calculate(10,2,"/")
calculate(10,2,"%")
calculate(10,2,"&")