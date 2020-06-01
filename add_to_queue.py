import sys


def add_to_queue(store, user):

    # write new user to queue
    file = open(f"{store}_queue.csv", "a")
    file.write(f"{priority_score},{user},{time.time()}\n")
    file.close()


print(add_to_queue(sys.argv[1], sys.argv[2]))
