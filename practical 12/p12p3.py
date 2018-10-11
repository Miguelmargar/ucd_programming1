# create approximation function
# ask user for number and for tolerance
# if user input numbers are negative:
#     print message
# else:
#     call function



def aprox(num, tol):
    # set the step and the root
    step = tol ** 2
    root = 0.0
    # while loop to check conditions
    while abs(num - root ** 2) >= tol and root ** 2 <= num:
        #print result
        print(root)
        # add step to root
        root += step
    print(root)
    
number = float(input("Please enter a positive number: "))
tolerance = float(input("Please enter a positive tolerance number: "))

if number <= 0 or tolerance <= 0:
    print("Please enter a positive number")
else:
    aprox(number, tolerance)