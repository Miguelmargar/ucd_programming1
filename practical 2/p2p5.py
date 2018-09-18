animals = "head of elephants"

head = animals[:4]
of = animals[5:8]
elephants = animals[8:]

print(head)
print(of)
print(elephants)

question_a = animals[1:1]
question_b = animals[2:1]
question_c = animals[:1] 
question_d = animals[1:] 
question_e = animals[:]  

print("answers to excercise 5:")

print("Answer question_a: nothing happens or is printed")
print("Answer question_b: nothing happens or is printed")
print("Answer question_c: it begins indexing from the 1st character ([0]) when x is omitted")
print("Answer question_d: it ends indexing up to and including the last character ([-1]) when y is omitted")
print("Answer to question_e: prints the entire string" )