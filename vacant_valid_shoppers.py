import sys


def vacant_valid_shoppers(store):

    # retrieve current number of valid shoppers
    file = open(f"{store}_valid_shoppers.csv", "r")
    num_valid_shoppers = len([line.strip() for line in file.readlines()])
    file.close()

    # retrieve current number of shoppers
    file = open(f"{store}_current_shoppers.csv", "r")
    num_shoppers = len([line.strip().split(",") for line in file.readlines()])
    file.close()

    # retrieve store capacity
    file = open(f"companies.csv", "r")
    companies = [line.strip().split(",") for line in file.readlines()]
    file.close()
    for company in companies:
        if company[0] == store:
            capacity = int(company[3])
            break

    if capacity - num_shoppers - num_valid_shoppers > 0:
        return "True"
    else:
        return "False"


print(vacant_valid_shoppers(sys.argv[1]), end="")
