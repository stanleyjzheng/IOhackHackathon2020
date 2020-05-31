from legitness import *
import threading


# populate user database
# people = int(input("Number of people: "))
# for i in range(people):
#     new_user()

# populate company database
# for i in range(2):
#     new_company()

# login
# user = login()
import random
user = random.randint(1, 10)

# choose company and location
file = open("companies.csv", "r")
companies = [company.strip().split(",") for company in file.readlines()]
company_names = [company[1] for company in companies]
print("Store Options: ")
for company_name in company_names:
    if company_name != "Company":
        print(company_name)
user_pick = input("Store: ")
while user_pick not in company_names:
    user_pick = input("Store: ")

# find store id
for company in companies:
    if company[1] == user_pick:
        store = company[0]
        break

print(store, user)

# add to queue
add_to_queue(store, user)
add_to_queue(store, user)

# retrieve queue
queue = retrieve_queue(store)

# repeat while the user is in the queue
while user in queue:
    # retrieve queue
    queue = retrieve_queue(store)
    # determine if someone has left the store and the next person is queue is the user
    if change_in_current_shoppers(store, user) and next_in_queue(store) == user:
        # remove the user from the queue
        remove_from_queue(store, user)
        add_to_valid_shoppers(store, user)

time_to_enter = threading.Timer(300.0, remove_from_valid_shoppers)
time_to_enter.start()

while True:
    stop = input("Stop the timer: ")
    enter = input("User entered store? ")
    if stop == "y" or enter == "y":
        time_to_enter.cancel()
        remove_from_valid_shoppers(store, user)
        break
