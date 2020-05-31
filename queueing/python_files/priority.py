import sys


def priority(total_time, user_priority, store):
    return store * total_time + user_priority


print(priority(sys.argv[1], sys.argv[2], sys.argv[3]))
