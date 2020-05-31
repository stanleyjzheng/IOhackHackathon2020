def next_in_queue(store):
    """
    Returns the person in queue priority 1 for a given store.
    """
    first_line = open(f"{store}_queue.csv", "r").readline().strip().split(",")
    return first_line[1]