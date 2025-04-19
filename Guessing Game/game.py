from random import randint

#error checking
while True:
    level = input("Level: ")
    if level.isalpha():
        continue
    elif int(level) < 1:
        continue
    else:
        break

level = int(level)
answer = randint(1, level)

while True:
    guess = input("Guess: ")
    if guess.isdigit() and int(guess) > 0:
        if int(guess) > answer:
            print("Too large!")
        elif int(guess) < answer:
            print("Too small!")
        else:
            print("Just right!")
            break
    elif guess.isalpha():
        continue
    elif int(guess) <= 0:
        continue


