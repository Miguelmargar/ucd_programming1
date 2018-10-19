#program to test if the word code is in a string given by user

def code_check(str):
    """checks to see if string code is within the string given by user
    
    assumes a string given by user
    it is case sensitive
    """
    #set up counter and word needed to be matched
    code = "code"
    count = 0
    #loop through the range of the string
    for i in range(len(str)):
        #if the string in the loop is code add to count
        if str[i : i + 4] == code:
            count += 1
    return count

#ask user for input string
str = input("Enter a string: ")

print("the string count is:", code_check(str))