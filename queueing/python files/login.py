def authenticate(username, password):
    file = open("accounts.csv", "r")
    accounts = [line.strip().split(",") for line in file.readlines()]
    file.close()
    for account in accounts:
        if account[3] == username and account[4] == password:
            return True
    return False


def login():
    username = input("Username: ")
    password = input("Password: ")
    while not authenticate(username, password):
        print("Wrong username or password.")
        username = input("Username: ")
        password = input("Password: ")
    print("Access granted.\n")
    file = open("accounts.csv", "r")
    accounts = [line.strip().split(",") for line in file.readlines()]
    file.close()
    for account in accounts:
        if account[3] == username:
            return account[0]