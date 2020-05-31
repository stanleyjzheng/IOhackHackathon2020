import sys


def leaving_store(store, user):
    # remove the person from file containing current shoppers
    file = open(f"{store}_current_shoppers.csv", "r+").readlines()
    current_shoppers = [line.strip() for line in file]
    current_shoppers.remove(user)
    file.close()

    file = open(f"{store}_current_shoppers.csv", "w")
    for person in current_shoppers:
        file.write(f"{person}\n")
    file.close()

    # get store capacity details
    file = open(f"companies.csv", "r").readlines()
    coloumn = [line.strip().split(",") for line in file]
    for row in coloumn:
        if store == row[0]:
            store_priority = row[1] * 0.95
    file.close()

    # update queue time for rest of shoppers at store location
    now = time.time()
    file = open(f"{store}_queue.csv", "a+").readlines()
    queue = [line.strip().split(",") for line in file]
    for line in queue:
        start_time = line[2]
        total_time = now - start_time
        line[0] = priority(total_time, user, store_priority)
    file.close()

    # write sorted queue to csv file
    file = open(f"{store}.csv", "w")
    for person in queue:
        file.write(f"{person[0]},{person[1]}\n")
    file.close()


print(leaving_store(sys.argv[1], sys.argv[2]))
