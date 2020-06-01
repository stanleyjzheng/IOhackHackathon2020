import sys


def capacity_left(store):

    # retrieve current number of shoppers
    file = open(f"{store}_current_shoppers.csv", "r")
    num_shoppers = len([line.strip().split() for line in file.readlines()])
    file.close()

    # retrieve store capacity
    file = open(f"companies.csv", "r")
    companies = [line.strip().split() for line in file.readlines()]
    for company in companies:
        if company[0] == store:
            capacity = int(company[3])
            break

    return capacity - num_shoppers


print(capacity_left(sys.argv[1]), end="")
