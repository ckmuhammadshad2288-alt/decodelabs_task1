import random
import string

while True:
    print("\n1) Generate a password  2) Check pass>
    choice = input("Choose: ")

    if choice == "1":
        length = int(input("Length (min 6): "))
        if length < 6:
            print("Too short! Use at least 6.")
        else:
            chars = string.ascii_letters + string.>
            password = ""
            for i in range(length):
                password = password + random.choic>
            print("Your password:", password)

    elif choice == "2":
        pwd = input("Enter password: ")
        score = 0

        if len(pwd) >= 8:
            score = score + 1
        if any(c.islower() for c in pwd):
            score = score + 1
        if any(c.isupper() for c in pwd):
            score = score + 1
        if any(c.isdigit() for c in pwd):
            score = score + 1
        if any(c in string.punctuation for c in pw>
            score = score + 1

        if score <= 2:
            print("Weak")
        elif score <= 4:
            print("Medium")
        else:
            print("Strong")

    elif choice == "3":
        print("Bye!")
        break

    else:
        print("Pick 1-3.")
