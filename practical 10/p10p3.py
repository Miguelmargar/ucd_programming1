"""
ask for user input
set counter
if user input == empty string
    print message
else:
    for i in user input:
        if i == vowels:
            counter up by 1
    print counter
"""



word = input("please enter a word: ")

vowels_count = 0

if word == "":
    print("program finished! please try again!")
else:
    for i in word:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            vowels_count += 1
    print("number of vowels is:", vowels_count)