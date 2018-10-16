import time
start_time = time.time()
#please check time.txt file for results

# define function with recursive nature to find factorial
# ask user for input number
# if user input less or equal to 0:
#     print message
# else:
#     call function within print statement to print result
# print time

def factorial(num):
    #to check all steps
    print(num)
    # base value to stop infinite recursion
    if num == 0:
        return 1
    else:
        #recursive function num * itself minus 1 to call itself
        return num * factorial(num - 1)


number= int(input("Please input a number: "))

if number <= 0:
    print("the number is negative, needs to be positive")
else:
    print(factorial(number))
    #print time taken for function to work out result
print("My program took", time.time() - start_time, "to run")
    
    
