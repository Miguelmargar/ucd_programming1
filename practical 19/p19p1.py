#Program to change int from base 10 to any other base
#prompts use for base 10 number and new base to return new base number
#answer done by reading http://ice-web.cc.gatech.edu/ce21/1/static/thinkcspy/Recursion
#/ConvertinganIntegertoaStringinAnyBase.html


def change_base(num,base):
    """Transforms num to new base given by base
    
    Assumes num and base are intergers
    recursively reduces num with division to its base value of num being smaller than the base required
    """
    #set the possible num options as a string
    string = "0123456789ABCDEF"
    #set base case
    if num < base:
        return string[num]
    else:
        #reduce the number with division and its mod down to base case
        return change_base(num // base, base) + string[num % base]

    
number = int(input("Enter a number: "))
base = int(input("Enter the required base: "))

print(change_base(number, base))

