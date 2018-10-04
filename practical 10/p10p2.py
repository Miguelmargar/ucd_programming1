"""
ask user input

if user input == 0:
    print message
elif user input < 0:
    create new_num = - user input
else:
    new_num = number
    
create counter
while counter cubed < new_num:
    counter up by 1
    if counter cubed == new_num:
        print message
    else:
        print message
"""



number = int(input("please type a number: "))

if number == 0:
    print("program finished, number has to be positive")
elif number < 0:
    new_num = -number
else:
    new_num = number 
    
number_check = 0
while number_check ** 3 < new_num:
    number_check += 1
   
    if number_check ** 3 == new_num:
        print(number_check, "is a perfect cube root of", new_num)
    else:
        print(number_check, "is not a perfect cube of", new_num)