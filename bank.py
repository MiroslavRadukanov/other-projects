haveacc = input("Do you have existing account in MiroBank? (yes/no) ")

if haveacc.lower() == "yes":
    print("Download users.txt and try with (test, 12345678)")
    user = input("Enter username: ")
    password = input("Enter password: ")
    found = False

    with open("/storage/emulated/0/Download/users.txt", "r") as f:
        for line in f:
            usr, pwd, balance = line.strip().split(",")
            if usr == user and pwd == password:
                found = True
                print(f"You are in! Your balance is {balance}$.")
                break

    if not found:
        print("Invalid username or password!")

elif haveacc.lower() == "no":
    usertaken = True
    while usertaken:
        user = input("Enter username: ")
        password = input("Enter password: ")
        usertaken = False

        with open("/storage/emulated/0/Download/users.txt", "r") as f:
            for line in f:
                usr, pwd, bal = line.strip().split(",")
                if usr == user:
                    print(f"Unsuccessful registration! The username {user} is already taken. Try again!")
                    usertaken = True
                    break

        if not usertaken:
            balance = 5000
            with open("/storage/emulated/0/Download/users.txt", "a") as f:
                f.write(f"\n{user},{password},{balance}")
            print("Registration successful!")
