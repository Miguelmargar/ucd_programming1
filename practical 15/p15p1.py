#define function


def other(num):
    ''' Recursive function to find a series of numbers'''
    
    #base case
    if num == 1:
        return 2
    else:
        # print current number to check progress
        print("the current number is:", num)
        # recursive function
        return num + other(num - 1)
        
#ask user input
user = int(input("please type a positive number for range: "))


#check the user input for positive number
if user < 0:
    print("error, it needs to be a positive number")
else:
    # if user input positive loop through range 
    while user > 0:
        print("Series output")
        #loop through each item in the range
        for i in range(1, user + 1):
            print("number in the series:", other(i))
        #ask user input until negative number given
        user = int(input("please type a positive number for range: "))
    else:
        print("Plese enter a positive integer")