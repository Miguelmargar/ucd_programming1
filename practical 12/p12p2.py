# create function to find print fibonacci series
# ask the user for length of the fibonacci series required
# if lenght in equal or less than 0:
#     print message
# else:
#     call fibonacci function

def fibonacci(num):
    # set fibonacci 1 and 2
    fib_0 = 0
    fib_1 = 1
    # print fibonacci 1 and 2
    print(fib_0, ",", fib_1, end = " ")
    # loop through range and make adjustments to variables accordingly
    for i in range(2, num + 1):
        fib = fib_0 + fib_1
        fib_0 = fib_1
        fib_1 = fib
        # print fib for each i
        print(",", fib, end = " ")
    # line brake
    print()
        
number = int(input("Please enter a positive number: "))

if number <= 0:
    print("Please enter a positive number")
else:
    fibonacci(number)
            
        