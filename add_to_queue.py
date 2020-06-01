import sys
import time


def add_to_queue(store, user):
    """
    Adds a user to queue and then sorts the queue for a given store.
    """
    import random
    priority_score = random.randint(1, 100)  # priority(total_time, user_priority, store)

    # write new user to queue
    file = open(f"{store}_queue.csv", "a")
    file.write(f"{priority_score},{user},{time.time()}\n")
    file.close()

    # sort queue
    def first_element(element):
        return int(element[0])

    file = open(f"{store}_queue.csv", "r")
    queue = [tuple(line.strip().split(",")) for line in file.readlines()]
    queue.sort(key=first_element, reverse=True)
    file.close()

    # write sorted queue to csv file
    file = open(f"{store}_queue.csv", "w")
    for person in queue:
        file.write(f"{person[0]},{person[1]},{person[2]}\n")
    file.close()


print(add_to_queue(sys.argv[1], sys.argv[2]))
