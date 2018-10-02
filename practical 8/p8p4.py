"""
ask user input 

if user input is less than 0:
    print message
else:
    set counters for each range to 0
    while the number is >= 0
        if number is 0:
            print message
            increase it's counter
        if number is between range:
            print message
            increase it's counter
        repeat ifs until needed
        increase count by 1
        ask user for input again
print the total counts
"""

number = int(input("please type your required number: "))

if number < 0:
    print("The number you input is negative")
else:
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    count5 = 0
    count6 = 0
    count7 = 0
    while number >= 0:
        if number == 0:
            print("number is 0")
            count1 += 1
        elif number > 0 and number <= 20:
            print("Number is greater than 0 and less than or equal to 20")
            count2 += 1
        elif number > 20 and number <= 40:
            print("Number is greater than 20 and less than or equal to 40")
            count3 += 1
        elif number > 40 and number <= 60:
            print("Number is greater than 40 and less than or equal to 60")
            count4 += 1
        elif number > 60 and number <= 80:
            print("Number is greater than 60 and less than or equal to 80")
            count5 += 1
        elif number > 80 and number <= 100:
            print("Number is greater than 80 and less than or equal to 100")
            count6 += 1
        elif number > 100:
            print("Number is greater than 100")
            count7 += 1
        number = int(input("please type your required number: "))
print(count1, "times you input 0")
print(count2, "times in range 1 to 20")
print(count3, "times in range 21 to 40")
print(count4, "times in range 41 to 60")
print(count5, "times in range 61 to 80")
print(count6, "times in range 81 to 100")
print(count7, "times you input more than 100")