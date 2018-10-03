"""
ask user for available_toppings
ask user for toppings_per_pizza

if available_toppings >= to toppings_per_pizza:
    x = factorial of available_toppings
    
    y = factorial of toppings_per_pizza
    
    z = factorial of available_toppings - toppings_per_pizza
    
    a = x / (z * y)
    
    print a
else:
    print error message
"""

available_toppings = int(input("please type a possible number of toppings: "))
toppings_per_pizza = int(input("please type toppings per pizza: "))

if available_toppings >= toppings_per_pizza:
    
    fact_available = 1
    for i in range(1, available_toppings + 1):
        fact_available *= i
        
    fact_pizza = 1
    for i in range(1, toppings_per_pizza + 1):
        fact_pizza *= i
    
    rest = available_toppings - toppings_per_pizza
    fact_rest = 1
    for i in range(1, rest + 1):
        fact_rest *= i
    
    possible = fact_available / (fact_rest * fact_pizza)
    
    print(possible)

else:
    print("Error! toppings available have to be more than toppings allowed per pizza!")
