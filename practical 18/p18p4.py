# program to check one string is in the end of the other

def strings(str1, str2):
    """checks for one string to be in the end of the other
    
    assumes two strings given
    irrelevant to lower or higher case
    """
    #transfor strings to lower case to avoid uppper case incompatibility
    low1 = str1.lower()
    low2 = str2.lower()
    
    # if low1.endswith(low2) or low2.endswith(low1):
    #     return True

    #find the length of both strings
    len1 = len(low1)
    len2 = len(low2)
    
    #test for compliance of the length of one string to be at the end of the other
    if low1 == low2[(len2-len1):] or low2 == low1[(len1-len2):]:
        return True

#ask user for two strings
str1 = input("Enter a string: ")
str2 = input("Enter another string: ")

#call function and print
print(strings(str1, str2))