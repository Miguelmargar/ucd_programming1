string = input("Please enter a word: ")


dog = 0
cat = 0
for i in range(len(string)):
    if string[i:i+3] == "dog":
        dog += 1
    if string[i:i+3] == "cat":
        cat += 1
if dog == cat:
    print("dog amount:", dog, ", is the same as cat amount:", cat)
else:
    print("dog amount:", dog, ", is NOT the same as cat amount:", cat)