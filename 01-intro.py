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
    Employee_Id= 6798065
    First_Name= "Johnson"
    Last_Name= "Ojo"
    Basic_Salary= 200000
    Allowance=5000
    Pension_Scheme=1000
    Tax= (5 / 100) * Basic_Salary
    Net_Salary=((Basic_Salary - Tax - Pension_Scheme) + Allowance)
    print(f'Employee {First_Name} {Last_Name} with id number {Employee_Id} has a monthly basic salary of {Net_Salary} USD')

calculateBasicSalary()

