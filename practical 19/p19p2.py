#Program to return any number in any base(including hexadecimal) into base 10
#has been worked out by checking from stack overflow

def base_ten(num, base):
    """Returns given number as base ten
    
    Assumes a number as a string which can contain letters for hexadecimal numbers
    Expects to be given the base of the number that needs to be translated to decimal
    
    """
    return int(num, base)
    

number = (input("Please enter a number: "))
base = int(input("Please enter a base: "))

print(base_ten(number, base))