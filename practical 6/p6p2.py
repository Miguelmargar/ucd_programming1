# ask user for the numbers

# allocated an empty variable
# if 1st number is odd:
#     give empty variable input number 1
# if 2nd number is odd:
#     give empty variable input number 2
# if 3rd number is odd:
#     give empty variable input number 3



num1 = int(input("please enter the 1st number:"))
num2 = int(input("please enter the 2nd number:"))
num3 = int(input("please enter the 3rd number:"))

highest = 0

if (num1%2 != 0):
    highest = num1
if (num2%2 != 0) and num2 > highest:
    highest = num2
if (num3%2 != 0) and num3 > highest:
    highest = num3

print(highest)
