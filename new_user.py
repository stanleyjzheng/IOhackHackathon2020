import sys


def new_user(first_name, last_name, email, password, phone_number, age, health_conditions):
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
    file.write(f"{user_id},{first_name},{last_name},{email},{password},{phone_number},{age},{health_conditions}\n")
    file.close()


print(new_user(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7]))
