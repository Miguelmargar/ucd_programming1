f = open("index.html", "r")
file = f.read()
f.close()

leftbracket = 0
rightbracket = 0
newline = 0
e = 0
startcomm = 0
endcomm = 0

for i in range(len(file)):
    if file[i:i+4] == "<!--":
        startcomm += 1
    if file[i] == "<":
        leftbracket += 1
    if file[i] == ">":
        rightbracket += 1
    if file[i] == "\n":
        newline += 1
    if file[i] == "e":
        e += 1
    if file[i:i+3] == "-->":
        endcomm += 1

# print(file)

# print(leftbracket)
# print(rightbracket)
# print(newline)
# print(e)
# print(startcomm)
# print(endcomm)

r = open("results.txt", "w")

r.write(str(leftbracket))
r.write("\n")
r.write(str(rightbracket))
r.write("\n")
r.write(str(newline))
r.write("\n")
r.write(str(e))
r.write("\n")
r.write(str(startcomm))
r.write("\n")
r.write(str(endcomm))

r.close()