# Show the Fibonacci series using recursive functions

def fibonacci(num):
   """Recursive function to print Fibonacci sequence"""
   if num <= 1:
        return num
   else:
        print("this is the current check: ", num)
        return(fibonacci(num-1) + fibonacci(num-2))


user = int(input("How many terms? "))

# check if the number of terms is valid
if user <= 0:
   print("Plese enter a positive integer")
else:
    while user > 0:
        print("Fibonacci series:")
        for i in range(user):
            print("Number in the series:", fibonacci(i))
        user = int(input("How many terms? "))
    else:
        print("Plese enter a positive integer")     
       