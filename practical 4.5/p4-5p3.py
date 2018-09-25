amount = int(input("Please enter amount:"))
big = (amount / 100) * 60
small = (amount / 100) * 40
tax_a = 23
tax_b = 41

tax_a_on_big = (big / 100) * tax_a
tax_b_on_small = (small / 100) * tax_b

if amount >= 0:
    print("amount: " , amount)
    print("tax on big: ", tax_a_on_big)
    print("tax on smal: ", tax_b_on_small)
    print("total amount of tax: ", tax_a_on_big + tax_b_on_small)
    print(amount - tax_a_on_big - tax_b_on_small)
else:
    print("Amount of income must be >= 0. Please try again.")