"""
. Write a program that prompts the user for a positive integer and uses a for loop to calculate
the factorial of that number.

"""

number = int(input("please type a positive number: "))

if number < 0:
    print("error, number is less than 0")
else:
    if number == 0:
        fact = 1
    elif number == 1:
        fact = 1
    else:
        fact = 1
        for i in range(1, number + 1):
            fact *= i
            
    print("the factorial of", number, "is:", fact)