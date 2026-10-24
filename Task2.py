balance = 0
total_spent = 0

while True:
    print("\n1) Add money  2) Add expense  3) Show>
    choice = input("Choose: ")

    if choice == "1":
        amount = float(input("Money to add: "))
        if amount > 0:
            balance = balance + amount
            print("Added!")
        else:
            print("Enter a positive amount.")

    elif choice == "2":
        amount = float(input("Expense amount: "))
        if amount > 0:
            if amount <= balance:
                balance = balance - amount
                total_spent = total_spent + amount
                print("Expense added!")
            else:
                print("Not enough balance!")
        else:
            print("Enter a positive amount.")

    elif choice == "3":
        print("Balance:", balance)
        print("Total Spent:", total_spent)

    elif choice == "4":
        break

    else:
        print("Pick 1-4.")
