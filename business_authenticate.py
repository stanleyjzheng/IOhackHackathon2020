import sys


def authenticate(username, password):
    file = open("companies.csv", "r")
    companies = [line.strip().split(",") for line in file.readlines()]
    file.close()
    for company in companies:
        if company[0] == str(username) and company[2] == str(password):
            return account[0]
    return "False"


print(authenticate(sys.argv[1], sys.argv[2]), end="")
