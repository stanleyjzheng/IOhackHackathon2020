import time
import threading


def new_user():
    # retrieve the last id
    file = open("accounts.csv", "r")
    data = file.readlines()
    file.close()
    if len(data) == 0:
        last_id = 0
    else:
        last_line = data[-1].strip().split(",")
        last_id = int(last_line[0])
    user_id = last_id + 1

    # create new user
    file = open("accounts.csv", "a")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")
    email = input("Email: ")
    password = input("Password: ")
    phone_number = input("Phone Number: ")
    file.write(f"{user_id},{first_name},{last_name},{email},{password},{phone_number}\n")
    file.close()


def new_company():
    # retrieve the last id
    file = open("companies.csv", "r")
    data = file.readlines()
    file.close()
    if len(data) == 1:
        last_company = 0
    else:
        last_line = data[-1].strip().split(",")
        print(last_line)
        last_company = int(last_line[0])
    company_id = last_company + 1

    # create new company
    file = open("companies.csv", "a")
    name = input("Company Name: ")
    wait_time = input("Average Wait Time: ")
    capacity = input("Max Capacity in Store: ")
    file.write(f"{company_id},{name},{wait_time},{capacity}\n")
    file.close()

    # create queue csv
    file = open(f"{company_id}_queue.csv", "w")
    file.close()

    # create current shoppers csv
    file = open(f"{company_id}_current_shoppers.csv", "w")
    file.close()

    # create valid shoppers csv
    file = open(f"{company_id}_valid_shoppers.csv", "w")
    file.close()


def priority(total_time, user_priority, store):
    return store * total_time + user_priority


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


def next_in_queue(store):
    """
    Returns the person in queue priority 1 for a given store.
    """
    first_line = open(f"{store}_queue.csv", "r").readline().strip().split(",")
    return first_line[1]


def remove_from_queue(store, user):
    # remove person from queue
    file = open(f"{store}_queue.csv", "r")
    queue = [tuple(line.strip().split(",")) for line in file.readlines()]
    for person in queue:
        if person[1] == user:
            queue.remove(person)
            break
    file.close()

    # write new queue to file
    file = open(f"{store}_queue.csv", "w")
    for person in queue:
        file.write(f"{person[0]},{person[1]},{person[2]}\n")
    file.close()


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


def remove_from_current_shoppers(store, user):
    # remove person from current shoppers
    file = open(f"{store}_current_shoppers.csv", "r")
    current_shoppers = file.readlines()
    current_shoppers.remove(user)
    file.close()

    # write new current shoppers to csv
    file = open(f"{store}_current_shoppers.csv", "w")
    for person in current_shoppers:
        file.write(f"{person}\n")
    file.close()


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


def remove_from_valid_shoppers(store, user):
    # remove person from valid shoppers
    file = open(f"{store}_valid_shoppers.csv", "r")
    valid_shoppers = [line.strip() for line in file.readlines()]
    print(valid_shoppers)
    valid_shoppers.remove(user)
    file.close()

    # write new valid shoppers to csv
    file = open(f"{store}_valid_shoppers.csv", "w")
    for person in valid_shoppers:
        file.write(f"{person}\n")
    file.close()


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


def authenticate(username, password):
    file = open("accounts.csv", "r")
    accounts = [line.strip().split(",") for line in file.readlines()]
    file.close()
    for account in accounts:
        if account[3] == username and account[4] == password:
            return True
    return False


def login():
    username = input("Username: ")
    password = input("Password: ")
    while not authenticate(username, password):
        print("Wrong username or password.")
        username = input("Username: ")
        password = input("Password: ")
    print("Access granted.\n")
    file = open("accounts.csv", "r")
    accounts = [line.strip().split(",") for line in file.readlines()]
    file.close()
    for account in accounts:
        if account[3] == username:
            return account[0]


def change_in_current_shoppers(store):
    file = open(f"{store}_current_shoppers.csv", "r")
    old_shoppers = file.readlines()
    file.close()

    global person_left
    person_left = False
    new_shoppers = old_shoppers

    while old_shoppers == new_shoppers:
        file = open(f"{store}_current_shoppers.csv", "r")
        new_shoppers = file.readlines()
        file.close()
    person_left = True


def retrieve_queue(store):
    file = open(f"{store}_queue.csv", "r")
    queue = [tuple(line.strip().split(",")) for line in file.readlines()]
    file.close()
    return queue
