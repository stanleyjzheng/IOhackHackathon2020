def remove_from_current_shoppers(store, user):
    # remove person from current shoppers
    file = open(f"{store}_current_shoppers.csv", "r")
    current_shoppers = file.readlines()
    current_shoppers.remove(user)
    file.close()

    # write new current shoppers to csv
    file = open(f"{store}_current_shoppers.csv", "w")
    for person in current_shoppers:
        file.write(f"{person}\n")
    file.close()