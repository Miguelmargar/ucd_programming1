"""
ask user input

set 1st num
set 2nd num

if user input <= to 0:
    print message
elif user input == 1:
    print message
else:
    print message start and stay in printed line
    set variables a, b, i to 1st num, 2nd num and 2
    while i is less than user input
        fibonacci is a + b
        print finoacci in while loop continued from previous print message
        set a to b
        set b to current fibonacci
        increase i by one
"""


limit = int(input("please type a positive number: "))

f_0 = 0
f_1 = 1

if limit <= 0: 
    print("Error: Number entered was less than or equal to 0") 
elif limit == 1: 
    print("Series is:", f_0) 
else: 
    print("Series is: ", f_0, ", ", f_1, sep = "", end = "")
    a, b, i = f_0, f_1, 2 
    
    while i < limit:
        fib = b + a 
        print(",", fib, end = "")
        a = b 
        b = fib 
        i += 1
print()