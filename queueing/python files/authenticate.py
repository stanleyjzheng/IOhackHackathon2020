import sys


def authenticate(username, password):
    file = open("accounts.csv", "r")
    accounts = [line.strip().split(",") for line in file.readlines()]
    file.close()
    for account in accounts:
        if account[3] == username and account[4] == password:
            return account[0]
    return False


pritn(login(sys.argv[1], sys.argv[2]))
