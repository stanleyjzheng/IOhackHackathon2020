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