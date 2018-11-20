from random import choice

fh = open("words.txt", "r")
words = [line[:-1] for line in fh]
fh.close()

word = choice(words)
length = len(word)

hide_word = list("_" * length)
print(hide_word)

# guess = input("please guess a letter: ")

counter = length

lives = 6
while ("_" in hide_word):
    guess = input("please guess a letter: ")
    if guess in word:
        print("your guess is correct!")
        for i in range(len(word)):
            if word[i] == guess:
                hide_word[i] = guess
        print(hide_word)
        print()
    else:
        print("your guess is incorrect!")
        print(hide_word)
        print()
        lives -= 1
        print("you have", lives, "left!")
        if lives == 0:
            break
        
if "_" not in hide_word:
    print("Congratulations you got the entire word!")
elif lives == 0:
    print("You lost all your lives!")
    
    

    
    





    




