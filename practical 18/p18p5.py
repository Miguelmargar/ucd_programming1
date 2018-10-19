#program to check that xyz is in string given by user but not .xyz

def xyz(str):
    """check whether the string .xyz is not in the string given by user but string xyz without . is
    
    assumes a string is given
    
    """
    #set up wrong and right
    wrong = "."
    right = "xyz"
    #loop through the range of the string up to and not including index -2
    for i in range(len(str) -2):
        #if the string contains right and then contains wrong do nothing
        if str[i:i+3] == right:
            if str[i-1] == ".":
                pass
            #else return true
            else:
                return True
        
#ask user for input
str = input("Enter a string: ")

print(xyz(str))