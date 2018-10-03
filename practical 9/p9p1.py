"""
ask user for input
set counter to 0
set total to 0

while counter is less or equal to user input:
    increase counter by 1
    add counter to total
print total
"""

number = int(input("please type a positive number: "))
counter = 0
total = 0

while counter <= number:
    counter += 1
    total += counter
    
    
print("The sum is:", total)