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
# i = 0
# for i in range(0, number + 1):
#     j = 0
#     for j in range(0, number + 1):
#         print (i + j, " ", end = " ")
#         j += 1 
#     print()
#     i += 1
  
# multiplication table - while
# i = 0
# while i <= number:
#     j = 0
#     while j <= i:
#         print(j * i, " ", end = " ")
#         j += 1
#     print()
#     i += 1
    
# multiplication table - for loop    
# for i in range(1, number + 1):
#     for j in range(1, i + 1):
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