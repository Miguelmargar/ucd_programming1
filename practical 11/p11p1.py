"""
ask user input
if user input less than 0:
    new_variable = -user input
else:
    new_variable = user input
    
fact = 1
loop for i in range (1 to new_variable + 1):
    up fact by 1
    
print message required
"""


number = int(input("please type a positive number: "))

if number < 0:
    new_number = -number
else:
    new_number = number
    
fact = 1
for i in range(1, new_number + 1):
    fact *= i
    
print("factorial of ", number, "is:", fact)