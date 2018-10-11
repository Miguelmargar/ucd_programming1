def f(x):
    print("Inside")
    x += 1 
    y = 1
    z = 2
    t = 10
    print("x is", x) 
    print("y is", y) 
    print("z is", z) 
    print("t is", t)
    return x
    
x, y, z, t = 5, 10, 15, 1661

print("before") 
print("x is", x) 
print("y is", y) 
print("z is", z)
print("t is", t)

z = f(x)
print("after") 
print("x is", x) 
print("y is", y) 
print("z is", z)
print("t is", t)