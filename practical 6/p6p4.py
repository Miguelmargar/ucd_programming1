# set password
# set counter for amount of tries

# while the amount of tries is less than 3:
#     ask for user input
#     if user input equal to set password:
#         print message
#         break
#     
#     increase count
#     
# if counter is 3:
# print message


        

password = "hello"
tries = 0


while tries < 3:
   
    user_input = input("Please enter your password: ")
   
    if user_input == password:
        print("You have successfully logged in")
        break
    
    tries += 1
        
if tries == 3:
    print("You have been denied access.")
    
    
