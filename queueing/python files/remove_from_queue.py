import sys


def remove_from_queue(store, user):
    # remove person from queue
    file = open(f"{store}_queue.csv", "r")
    queue = [tuple(line.strip().split(",")) for line in file.readlines()]
    for person in queue:
        if person[1] == user:
            queue.remove(person)
            break
    file.close()


print(remove_from_queue(sys.argv[1], sys.argv[2]))
