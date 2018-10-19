#Ask user for input number
# check for number more or equals to 0
#create empty tuple to add numbers
#loop through numbers in range 1 to user input number
#   if user input number is mod to each iteration in the range
#       add this number to total


num1 = int(input("Enter a positive integer: ")) 



if num1 <= 0:
    print("Needs to be a positive number")
else:
    total = ()
    for i in range(1, num1):
        if num1 % i == 0:
            total += (i,)
    print(total)