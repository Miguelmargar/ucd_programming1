def aprox(num, tol):
    step = tol ** 2
    root = 0.0
    while abs(num - root ** 2) >= tol and root ** 2 <= num:
        print(root)
        root += step
    print(root)
    
number = float(input("Please enter a positive number: "))
tolerance = float(input("Please enter a positive tolerance number: "))

if number <= 0 or tolerance <= 0:
    print("Please enter a positive number")
else:
    aprox(number, tolerance)