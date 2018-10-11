

def factorial(num):
    print(num)
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)


number= int(input("Please input a number: "))

if number <= 0:
    print("the number is negative, needs to be positive")
else:
    print(factorial(number))