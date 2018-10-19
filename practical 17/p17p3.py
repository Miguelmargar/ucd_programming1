# ask user for input
# set dog and cat counters
#loop through user input 

string = input("Please enter a word: ")

#set up counter for cat and dog
dog = 0
cat = 0
#loop through string to check for words needed
for i in range(len(string)-2):
    if string[i:i+3] == "dog":
        dog += 1
    if string[i:i+3] == "cat":
        cat += 1
if dog == cat:
    print("dog amount:", dog, ", is the same as cat amount:", cat)
else:
    print("dog amount:", dog, ", is NOT the same as cat amount:", cat)