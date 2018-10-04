
number = int(input("please type a positive number: "))

if number < 0:
    print("program finished, number has to be positive")
else:
    number_check = 0
    while number_check ** 2 < number:
        number_check += 1
        if number_check ** 2 == number:
            print(number_check, "is a perfect square root of", number)
        else:
            print(number_check, "is not a perfect square of", number)
    