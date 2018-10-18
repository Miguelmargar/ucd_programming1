# Program to get the common divisors of integers supplied by the user 
# Demonstrates the use of tuples
def findDivisors(num1):
    """Finds the common divisors of num1
    Assumes that num1 is positive integers Returns a tuple containing the common divisors of num1"""
    divisors = (1,) 
    for i in range(2, (num1 // 2) + 1): 
        if num1 % i == 0: 
            divisors += (i,)
            
    return divisors
    
number1 = int(input("Enter a positive integer: ")) 

if number1 <= 0: 
    print("Numbers should be > 0.") 
else:
    # First of all, get the common divisors and print them out 
    divisors = findDivisors(number1) 
    print("The common divisors of", number1, "is:", divisors)
    # Now sum them and print the total 
    total = 0 
    for d in divisors: 
        total += d 
    print("Sum of the divisor is:", total)
print("Finished!")