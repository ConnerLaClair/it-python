
import random


print("==================")
print(" Guess My Number  ")
print(" By Mr. La Clair  ")
print("==================")
print("")


name = input("What is your name? ")
print("")

guess = -1

print("I'm thinking of a number between 0 and 100. Can you guess it?")
the_number = random.randint(1,99)

while guess != the_number:
    guess_text = input("What is your guess? ")
    guess = int(guess_text)

    if guess < the_number:
        print(f"Sorry {name}, but your idiot guess is wrong XDDDDD, far too low, try again noob.")
    elif guess > the_number:
        print(f"Sorry {name}, you missed the battleship, They're not that high on ye horizon")
    else:
        print(f"You Beat The EnderDragon! Bet You Feel Real Tough Huh! Big Old {name}!")

print("Play Again Johnny Boi")