from banner import banner
banner("ZIP CODE SORTER","Conner LaClair")

print("Welcome to the Newaygo County zip code sorter.")

while True:
    zip_code = int(input("Please enter a zip code: "))
    if zip_code == 49309:
        print(f"The zip code {zip_code} is for Bitely.")
    elif zip_code == 49312:
        print(f"The zip code {zip_code} is for Brohman.")
    elif zip_code == 49337:
        print(f"The zip code {zip_code} is for Croton and Newaygo.")
    #
    #
    #
    else:
        print(f"The zip code {zip_code} is not in Newaygo County.")

    if input("Would you like to enter another zip code (Y/N)? ") == "Y":
        continue
    else:
        break

print("Thank you...")

