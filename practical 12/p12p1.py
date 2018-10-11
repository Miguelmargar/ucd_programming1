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
