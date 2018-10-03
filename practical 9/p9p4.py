"""
ask user for number

if number less than 0:
    print error message
else:
    while number > 0:
        set counter
        set factorial
        while counter <= number:
            if number == 0 or number == 1:
                factorial = 1
            else:
                fact *= counter
                increase counter by 1
            print the result message
            ask user for another input number
        else:
            print error message

"""

number = int(input("please type a number: "))

if number < 0:
    print("error, number is less than 0")
else:
    while number > 0:   
        counter = 1
        fact = 1
        while counter <= number:
            if number == 0:
                fact = 1
            elif number == 1:
                fact = 1
            else:
                fact *= counter
                counter += 1 
        print("the factorial of", number, "is:", fact)
        number = int(input("please type a number: "))
    else:
        print("error, number is less than 0")
    