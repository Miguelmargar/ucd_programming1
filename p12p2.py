def fibbonacci(num):
    fib_0 = 0
    fib_1 = 1
    print(fib_0, ",", fib_1, end = " ")
    for i in range(2, num + 1):
        fib = fib_0 + fib_1
        fib_0 = fib_1
        fib_1 = fib
        print(",", fib, end = " ")

    print()
        
number = int(input("Please enter a positive number: "))

if number <= 0:
    print("Please enter a positive number")
else:
    fibbonacci(number)
            
        