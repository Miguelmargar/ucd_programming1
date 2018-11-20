# ask user for year
number = int(input("type a year: "))

if number < 0:
    print("Year typed has to be positive, please run program again")
else:
    # find leap year:
    # if number is multiple of 4
    if number % 4 == 0:
        # if number is multiple of 100:
        if number % 100 == 0:
            # if year is multiple of 900:
            if number % 900 == 0:
# print messeges according to conditions being met
                print(number, "Is a leap year")
            else:
                print(number, "Is not a leap year")
        else:
            print(number, "Is a leap year")
    else:
        print(number, "Is not a leap year")