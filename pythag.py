import math

def banner(subject, author):
    subject_length = len(subject)
    by_line = f"By {author}"
    by_line_length = len(by_line)
    banner_length = max(subject_length, by_line_length) + 4
    print("-" * banner_length)
    print(f"{subject:^{banner_length}}   ")
    print(f"{by_line:^{banner_length}}   ")
    print("-" * banner_length)
    print("")


if __name__ == "__main__":
    banner("Hello World", "Conner La Clair")


print("We will help you find the missing side of a right triangle. The lengths of the two sides are 'a' and 'b',\nand the length of the hypothenuse is 'c'.")

while True:
    a = input("Please enter the 'a' value of the pythagorean theory: ")
    b = input("Please enter the 'b' value of the pythagorean theory: ")
    c = input("Please enter the 'c' value of the pythagorean theory: ")
    try:
        a = int(a)
    except:
        a = None
    try:
        b = int(b)
    except:
        b = None
    try:
        c = int(c)
    except:
        c = None

    if a == None and b!= None and c!= None:
        a = math.sqrt(c*c - b*b)
        print(f"Your missing side is a and its length is {a}")
    elif b == None and a!= None and c!= None:
        b = math.sqrt(c*c - a*a)
        print(f"Your missing side is b and its length is {b}")
    elif c == None and a!= None and b!= None:
        c = math.sqrt(a*a + b*b)
        print(f"Your missing side is c and its length is {c}")
    else:
        print("Your input is incorrect")

    if input("Would you like to calculate another triangle (Y/N)? ") == "Y":
        continue
    else:
        break
print("Thank you for using the Pythagorean Calculator")