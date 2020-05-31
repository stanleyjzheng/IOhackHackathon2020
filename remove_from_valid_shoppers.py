import sys


def remove_from_valid_shoppers(store, user):
    # remove person from valid shoppers
    file = open(f"{store}_valid_shoppers.csv", "r")
    valid_shoppers = [line.strip() for line in file.readlines()]
    print(valid_shoppers)
    valid_shoppers.remove(user)
    file.close()

    # write new valid shoppers to csv
    file = open(f"{store}_valid_shoppers.csv", "w")
    for person in valid_shoppers:
        file.write(f"{person}\n")
    file.close()


print(remove_from_valid_shoppers(sys.argv[1], sys.argv[2]))
