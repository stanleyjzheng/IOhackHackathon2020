def retrieve_queue(store):
    file = open(f"{store}_queue.csv", "r")
    queue = [tuple(line.strip().split(",")) for line in file.readlines()]
    file.close()
    return queue