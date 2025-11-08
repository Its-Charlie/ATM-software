print("Welcome to State Bank of India")
p = int(input("Enter your 4-digit PIN number: "))
m = 25000  # Available balance

if p == 1234:
    print("1 - Withdraw")
    print("2 - Balance Enquiry")
    print("3 - Fast Cash")

    c = int(input("Please choose a transaction: "))

    if c == 1:
        w = int(input("Enter withdraw amount: "))
        if w < m and w % 100 == 0:
            print("Please take your amount:", w)
        else:
            print("Invalid cash amount or insufficient balance.")

    elif c == 2:
        print("Your available balance is:", m)

    elif c == 3:
        print("1 -> 5,000")
        print("2 -> 10,000")
        print("3 -> 15,000")
        print("4 -> 20,000")
        f = int(input("Enter fast cash option: "))

        if f == 1 and 5000 <= m:
            print("Please take cash: 5000")
        elif f == 2 and 10000 <= m:
            print("Please take cash: 10000")
        elif f == 3 and 15000 <= m:
            print("Please take cash: 15000")
        elif f == 4 and 20000 <= m:
            print("Please take cash: 20000")
        else:
            print("Invalid fast cash option or insufficient balance.")

    else:
        print("Wrong transaction choice.")

else:
    print("Wrong PIN number.")
