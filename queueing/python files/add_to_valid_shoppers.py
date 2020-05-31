import sys


def add_to_valid_shoppers(store, user):
    """
    Adds a user to valid shoppers for a given store.
    """
    import random
    priority_score = random.randint(1, 100)  # priority(total_time, user_priority, store)

    # write new user to current shoppers
    file = open(f"{store}_valid_shoppers.csv", "a")
    file.write(f"{user}\n")
    file.close()


print(add_to_valid_shoppers(sys.argv[1], sys.argv[2]))
