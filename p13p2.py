# definition of function
def maximum(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
        

# calling of function

number_1 = int(input("Please input a number: "))
number_2 = int(input("Please input a number: "))

print(maximum(number_1, number_2))