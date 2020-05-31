import sys


def authenticate(username, password):
    file = open("accounts.csv", "r")
    accounts = [line.strip().split(",") for line in file.readlines()]
    file.close()
    for account in accounts:
        if account[3] == str(username) and account[4] == str(password):
            return account[0]
    return "ok"


print(authenticate(sys.argv[1], sys.argv[2]))
