"""
ask for user input

while user input less than 0:
    1st num = 0
    2nd num = 1
    
    if user input <= 0:
        print message
    elif user input == 1:
        print message
    else:
        print message with 1st and 2nd nums leave line open
        set a, b, i to 1st, 2nd nums and i
        
        for i in range(2 to user input):
            set fib to b + a
            print continued message
            set a to b
            set b to current fibonacci
    ask for user input
else:
    print error message
"""


limit = int(input("please type a positive number: "))


while limit > 0:
    f_0 = 0
    f_1 = 1
    
    if limit <= 0: 
        print("Error: Number entered was less than or equal to 0") 
    elif limit == 1: 
        print("Series is:", f_0) 
    else: 
        print("Series is: ", f_0, ", ", f_1, sep = "", end = "")
        a, b, i = f_0, f_1, 2 
        
        for i in range(2, limit):
            fib = b + a
            print(",", fib, end= "")
            a = b
            b = fib
    print()
    limit = int(input("please type a positive number: "))         
else:
    print("Error: Number entered was less than or equal to 0")