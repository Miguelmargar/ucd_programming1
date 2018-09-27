"""
set total to 0

loop i through range(1, 10000):
    if i mod 3 or i mod 5:
        add i to total
Print total
"""

total = 0

for i in range(1, 10000):
    if i%3 == 0 or i%5 == 0:
        total += i
print(total)