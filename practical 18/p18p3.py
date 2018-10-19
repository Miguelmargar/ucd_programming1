#program to count for strings containing co at 1st two strings and e at 4th string


def code_check(str):
    """finds co and e in a string with letters inbetween but no other characters
    
    assumes a string given
    
    """
    #check for string to be bigger than 4 carachters
    if len(str) < 4:
        print("The input needs to be at least four letters")
    else:
        #set requirements and counter
        start = "co"
        end = "e"
        abc = "abcdefghijklmnopqrstuvwxyz"
        ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        count = 0
        #loop through the string
        for i in range(len(str) -3):
            #if string meets requirements add to count
            if (str[i : i + 2] == start) and (str[i + 3] == end) and (str[i + 2] in abc or str in ABC):
                count += 1
        #return count result
        return count

#ask user for input
str = input("Enter a string: ")
#call function
print(code_check(str))
        