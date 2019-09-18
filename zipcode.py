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