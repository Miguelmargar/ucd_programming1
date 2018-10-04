limit = int(input("please type a positive number: "))

f_0 = 0
f_1 = 1

if limit <= 0: 
    print("Error: Number entered was less than or equal to 0") 
elif limit == 1: 
    print("Series is:", f_0) 
else: 
    print("Series is: ", f_0, ", ", f_1, sep = "", end = "")
    a, b, i = f_0, f_1, 2 
    
    while i < limit:
        fib = b + a 
        print(",", fib, end = "")
        a = b 
        b = fib 
        i += 1
print()