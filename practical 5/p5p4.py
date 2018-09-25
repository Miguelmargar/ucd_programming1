number = int(input("imput a number:"))

if number == 0:
    print("the number is 0")
elif number > 0 and number <= 20:
    print("the number is between 1 and 20")
elif number > 20 and number <= 40:
    print("the number is between 21 and 40")
elif number > 40 and number <= 60:
    print("the number is between 41 and 60")
elif number > 60 and number <= 80:
    print("the number is between 61 and 80")
elif number > 80 and number <= 100:
    print("the number is between 81 and 100")
elif number > 100:
    print("the number is bigger than 100")
else:
    print("number is negative")