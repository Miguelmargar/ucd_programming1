"""
ask for user input

for i in range(0 to user input + 1):
    user input == i
    
    work out 2 * user input
    work out user input + 1
    
    obtain fac_2n
    
    obtain fact_n_1
    
    obtain fact of user input
    
    user factorials above with formula
    
    print catalan results in for loop
"""

limit = int(input("please type a positive number: "))

for each in range(0, limit + 1):
    limit = each
    
    two_n = 2 * limit
    n_1 = limit + 1
    
    fact_2n = 1
    for i in range(1, two_n + 1):
        fact_2n *= i
    
    fact_n_1 = 1
    for i in range(1, n_1 + 1):
        fact_n_1 *= i
        
    fact_limit = 1
    for i in range(1, limit + 1):
        fact_limit *= i
        
    catalan = fact_2n / (fact_n_1 * fact_limit)
    
    print(catalan, " ", end = "")
print()
