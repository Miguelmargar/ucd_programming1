#Program to check the amount of each type of bracket in a file


def check_brackets():
    """Checks quantity of each type of braket in file given index.html
    
    Reads file and loops through it to compare each character with each type of bracket
    If the same amount of each bracket exists in the file it prints message as well as count of each bracket
    
    """
    #open, read and close file
    f = open("index.html", "r")
    file = f.read()
    f.close()
    
    # Set counter for each type of bracket
    l_p = 0
    r_p = 0
    l_l = 0
    r_l = 0
    l_d = 0
    r_d = 0
    less = 0
    more = 0
    
    #loop through file and add to each bracket's counter
    for i in (file):
        if  i == "(":
            l_p += 1
        if i == ")":
            r_p += 1
        if i == "[":
            l_l += 1
        if i == "]":
            r_l += 1
        if i == "{":
            l_d += 1
        if i == "}":
            r_d += 1
        if i == "<":
            less += 1
        if i == ">":
            more += 1
            
            
    # print count for each bracket        
    print("There are", l_p, "of ( brackets")
    print("There are", r_p, "of ( brackets")
    print("There are", l_l, "of [ brackets")
    print("There are", r_l, "of ] brackets")
    print("There are", l_d, "of { brackets")
    print("There are", r_d, "of } brackets")
    print("There are", less, "of < brackets")
    print("There are", more, "of > brackets")
    
    #if each type of bracket is corresponding in number to its equivalent or not print necessary message  
    if l_p == r_p and l_l == r_l and l_d == r_d and less == more:
        print("There are the same number of left and right brackets of each type")
    else:
        print("There aren't the same number of left and right brackets of each type")

check_brackets()