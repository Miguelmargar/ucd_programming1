"""
ask user for year
if year >= to 0:
    if (year mod 4 == 0 and year mod 100 != 0) or (year mod 400 == 0):
        print message
    else:
        print message
else:
    print message
"""



year = int(input("please type a date: "))

if year >= 0: 
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): 
        print (year , "is a leap year.") 
    else:
        print (year , "is not a leap year.") 
else: 
    print ("Year must be greater than 0.")
    
print (" Finished !")