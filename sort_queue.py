import sys
import time


def sort_queue(store):

    # create queue list from reading document
    file = open(f"{store}_queue.csv", "r")
    queue = [line.strip().split(",") for line in file.readlines()]
    file.close()

    # open accounts file
    file = open("accounts.csv", "r")
    accounts = [line.strip().split(",") for line in file.readlines()]
    file.close()

    # add personal priority to accounts
    for person in queue:
        for account in accounts:
            if account[0] == person[1]:
                priority = time.time() - float(person[0]) + int(account[8])
                person.append(priority)
                break

    # sort queue
    def last_element(element):
        return int(element[-1])
    queue.sort(key=last_element, reverse=True)

    # write sorted queue to csv file
    file = open(f"{store}_queue.csv", "w")
    for person in queue:
        file.write(f"{person[0]},{person[1]}\n")
    file.close()


print(add_to_queue(sys.argv[1]))