import random as rd

inf = int(input("Between : "))
sup = int(input("and : "))
assert(inf<=sup), "The inferior number should not be higher than the superior"

mysteryNb = rd.randint(inf, sup)
found = False
tries = 0
triesList = []

while not found:
    guess = int(input("Guess the mystery number : "))
    tries+=1
    triesList.append(guess)
    if guess > mysteryNb:
        print("Too high :(")
    elif guess < mysteryNb:
        print("Too low :(")
    elif guess == mysteryNb:
        print("Bravo ! You found it in only "+str(tries)+" tries.")
        print("Your tries : "+str(triesList))
        found = True