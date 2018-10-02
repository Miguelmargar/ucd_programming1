"""
ask user for input
set x to 1
while is less or equal to user input:
    set y to 1
        while y less or equal to user input:
            print y * x
            increase y
        empty line
        increase x
"""


number = int(input("please type a limit: "))

x = 1

while x <= number:
    y = 1
    while y <= number:
        print(y * x, "", end = "")
        y += 1
    print()
    x += 1


