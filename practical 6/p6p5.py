"""
set password
ask user for input

if user input equals password:
    print message
else:
    print message
    ask user input
    ask user input
    ask user input
    if userinput1 equal password and userinput2 equal password and userinput3 equal password:
        print message
    else:
        print message
"""


password = "hello"
    
user_input = input("please enter your password: ")
    
if user_input == password:
    print("You have successfully logged in")
    correct = "yes"
else:
    print("Sorry the password is wrong")
    try1 = input("please enter your password again: ")
    try2 = input("please enter your password again: ")
    try3 = input("please enter your password again: ")
    if try1 == password and try2 == password and try2 == password:
        print("You have successfully logged in")
    else:
        print("You have been denied access")