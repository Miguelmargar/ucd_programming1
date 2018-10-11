def print_max():
    def maximum(num1, num2):
        if num1 > num2:
            return num1
        else:
            return num2

    num1 = int(input("Please input a number: "))
    num2 = int(input("Please input a number: "))
    print("The biggest is:", maximum(num1, num2))

print_max()

    