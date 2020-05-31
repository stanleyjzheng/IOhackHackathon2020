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