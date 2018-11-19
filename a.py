number = int(input("type a number: "))

# addition table - while
# i = 0
# while i <= number:
#     j = 0
#     while j <= number:
#         print(i + j, " ", end = " ")
#         j += 1
#     print()
#     i += 1

# addition table - for loop
# for i in range(0, number + 1):
#     for j in range(0, number + 1):
#         print (i + j, " ", end = " ")
#     print()
  
# multiplication table - while
# i = 1
# while i <= number:
#     j = 1
#     while j <= i:
#         print(j * i, " ", end = " ")
#         j += 1
#     print()
#     i += 1
    
# multiplication table - for loop    
# for i in range(0, number + 1):
#     for j in range(0, i + 1):
#         print (j * i, " ", end = " ")
#     print()

# fibonacci - while
# fib_0 = 0
# fib_1 = 1
# count = 2
# print(fib_0, ",", fib_1, end = " ")
# while count <= number:
#     fib = fib_0 + fib_1
#     print(",", fib, end = " ")
#     fib_0 = fib_1
#     fib_1 = fib
#     count += 1
# print()

# fibonacci - for loop
# fib_0 = 0
# fib_1 = 1
# print(fib_0, ",", fib_1, end = " ")
# for i in range(0, number + 1):
#     fib = fib_0 + fib_1
#     print(",", fib, end = " ")
#     fib_0 = fib_1
#     fib_1 = fib
# print()

# factorial - while
# count = 1
# fact = 1
# while count <= number:
#     fact *= count
#     count += 1
# print(fact)

# factorial - for loop
# fact = 1
# for i in range(1,  number + 1):
#     fact *= i
# print(fact)

# factorial - recursive
# def fact(x):
#     if x == 0:
#         return 1
#     else:
#         return x * fact(x - 1)

# print(fact(number))

# find leap year:
# if number % 4 == 0:
#     if number % 100 == 0:
#         if number % 400 == 0:
#             print(number, "Is a leap year")
#         else:
#             print(number, "Is not a leap year")
#     else:
#         print(number, "Is a leap year")
# else:
#     print(number, "Is not a leap year")
   
   
# aproximate square root search
# epsilon = 0.5
# step = epsilon ** 2 # then this is 0.25

# root = 0.0
# # first condition works from the number given down
# # second condition works from the initial root value up to ensure that it does not go over the number to check
# while abs(number - root ** 2) >= epsilon and root ** 2 <= number: 
#     root += step

# if abs(number - root ** 2) < epsilon:
#     print("the aprox square root of", number, "is:", root)
# else:
#     print("failed to finish the square root of:", number)
    
# print("finished")
    

    
    
# print(number - root ** 2)
  
  
   