num1 = int(input("Enter a positive integer: ")) 



if num1 <= 0:
    print("Needs to be a positive number")
else:
    total = []
    for i in range(1, num1):
        if num1 % i == 0:
            total.append(i)
    print(total)