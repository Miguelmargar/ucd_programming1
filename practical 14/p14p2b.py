import time
start_time = time.time()
#please check time.txt file for results

# function finds the factorial of a number
# ask the user for input
# if user input less or equal to 0:
#     print message
# else
#     call function
# print time


def factorial(num):
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print("factorial of", num, "is:", fact)
  
    
number = int(input("Please enter a positive number: "))

if number <= 0:
    print("Please enter a positive number")
else:
    factorial(number)
#print time taken for function to work out result
print("My program took", time.time() - start_time, "to run")