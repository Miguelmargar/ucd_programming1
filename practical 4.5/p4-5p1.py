amount = int(input("please enter € amount to exchange:"))
dollar_rate = 1.18
pound_rate = 0.88
   
if amount >= 0: 
    print(amount * dollar_rate)
    print(amount * pound_rate)
else:
    print("The amount should be > or = 0, please try again")
    