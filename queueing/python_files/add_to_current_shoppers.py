import sys


def add_to_current_shoppers(store, user):
    """
    Adds a user to current shoppers for a given store.
    """
    import random
    priority_score = random.randint(1, 100)  # priority(total_time, user_priority, store)

    # write new user to current shoppers
    file = open(f"{store}_current_shoppers.csv", "a")
    file.write(f"{user}\n")
    file.close()


print(add_to_current_shoppers(sys.argv[1], sys.argv[2]))
