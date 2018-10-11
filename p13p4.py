def f(x):
    print("Inside")
    x += 1 
    y = 1 
    print("x is", x) 
    print("y is", y) 
    print("z is", z) 
    return x
    
x, y, z = 5, 10, 15

print("before") 
print("x is", x) 
print("y is", y) 
print("z is", z)

z = f(x)
print("after") 
print("x is", x) 
print("y is", y) 
print("z is", z)