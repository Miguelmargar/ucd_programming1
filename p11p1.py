number = int(input("please type a positive number: "))

if number < 0:
    new_number = -number
else:
    new_number = number
    
fact = 1
for i in range(1, new_number + 1):
    fact *= i
    
print("factorial of ", number, "is:", fact)