"""
ask user for input
set total to 0
for i in range 0 to user input + 1:
    increase total by i 
print total

"""

number = int(input("please type a positive number: "))

total = 0

for i in range(0, number + 1):
    total += i
print(total)