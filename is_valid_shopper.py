import sys


def is_valid_shopper(store, user):
    file = open(f"{store}_valid_shoppers.csv", "r")
    valid_shoppers = [line.stip().split(",") for line in file.readlines()]
    if user in valid_shoppers:
        return "True"
    else:
        return "False"


print(is_valid_shopper(sys.argv[1], sys.argv[2]))
