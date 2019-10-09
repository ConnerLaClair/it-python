
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






peter = 0
while peter != 10 and meg !=10
    print("griffen")
    peter += 1
    player_score += 1




print_welcome_message()




from banner import banner
play_again = input

banner("ZIP CODE SORTER","Conner LaClair")

print("Welcome to the Newaygo County zip code sorter. ")
user_choice = input("Please Enter Your Zip Code: ")

while play_again != {"Y"}:
    if user_choice != 49349:
        print(f"The zip code 49349 is for White Cloud")
    if user_choice == 49309:
        print(f"The zip code 49309 is for Bitely")
    if user_choice == 49312:
        print(f"The zip code 49312 is for Brohman")
    if user_choice == 49337:
        print(f"The zip code 49337 is for Croton")
play_again = input("Y,N")