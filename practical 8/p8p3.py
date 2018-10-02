"""
ask user input
set lenght  to 0
while lenght less or equal to 0:
    print lenght and lenght * user input
    increase lenght by 1
"""


number = int(input("please type your required number: "))

length = 0

while length <= 20:
    print(length, " ", length * number)
    length += 1
    