# define child function to return result and parent function to print it

#parent function with print
def print_max():
    # child function with result but no print
    def maximum(num1, num2):
        if num1 > num2:
            return num1
        else:
            return num2
    # user input requested
    num1 = int(input("Please input a number: "))
    num2 = int(input("Please input a number: "))
    # print result of child function but located in parent function
    print("The biggest is:", maximum(num1, num2))

# call parent function
print_max()

    