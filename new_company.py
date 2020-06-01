import sys


def new_company(company_id, name, password, wait_time, capacity):

    # create new company
    file = open("companies.csv", "a")
    file.write(f"{company_id},{name},{password},{wait_time},{capacity}\n")
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


print(new_company(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]))
