import math

length = int(input("Please enter the lenght:"))
radius = length / 2

print("Square area: ", length ** 2 )
print("Volume of cube: ", length ** 3)
print("Area of circle: ", math.pi * radius ** 2)
print("Volume of sphere: ", (4/3) * math.pi * (radius ** 3))
print("Volume of cylinder: ", math.pi * (radius ** 2) * length)
