"""
ask user for input  
if user input less or equal 0:
    print message
else
    while user input is more than 0:
        if mod 2:
            print message
        if mod 3:
            print message
        repeat for each mod
        ask user for input again

"""

number = int(input("please type a number: "))

if number <= 0:
    print("The number you input is negative")
else:
    while number > 0:
        if number%2 == 0:
            print(number, "is divisible by 2")
        elif number%3 == 0:
            print(number, "is divisible by 3")
        elif number%5 == 0:
            print(number, "is divisible by 5")
        elif number%7 == 0:
            print(number, "is divisible by 7")    
        number = int(input("please type a number: "))        

        
