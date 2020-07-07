totalcustomers = int(input("Enter the # of customer details b/w 1 and 105\n"))

list_ordertime = []
list_entrytime = []


def input_details(totalcustomers):
    while 1 == 1:
        if totalcustomers > 105 or totalcustomers < 1:
            print("The # of customers should be b/w 1 and 105")
            totalcustomers = int(input("Enter the # of customer details\n"))
            continue
        else:
            break

    totalcustomersnumber = totalcustomers
    while totalcustomersnumber > 0:
        customerdetails = input(
            "Enter the details of customers in following format ""5 2"", here 5 is the time required to make the order"
            "and 2 will be the time customer entered the Restaurant\n")
        while 1 == 1:
            if customerdetails[1] != ' ' or customerdetails[0] == ' ':
                print("Wrong format Re-Enter")
                customerdetails = input(
                    "Enter the details of customers in following format ""5 2"", here 5 is the time required to make the order"
                    "and 2 will be the time customer entered the Restaurant\n")
                continue
            else:
                break
        list_ordertime.append(customerdetails[0])
        list_entrytime.append(customerdetails[2])
        totalcustomersnumber = totalcustomersnumber - 1


def check_best_wait_time(list_ordertime, list_entrytime, totalcustomers):
    list_ordertime_local = list_ordertime
    waiting_time_individual = []

    dict_ordertime_entrytime = {}
    for values in range(totalcustomers):
        dict_ordertime_entrytime[str(list_ordertime[values])] = list_entrytime[values]

    print(dict_ordertime_entrytime)
    list_ordertime_local.sort()

    count_ordertime = 0
    for ordertime in list_ordertime_local:
        count_ordertime = count_ordertime + int(ordertime)
        waiting_time_individual.append(count_ordertime)

    index = 0
    for ordertime in list_ordertime_local:
        waiting_time_individual[index] = waiting_time_individual[index] - int(dict_ordertime_entrytime.get(str(ordertime)))
        index = index + 1

    print("Waiting Time for each individual ", waiting_time_individual)

    total_watingtime = 0
    for waitingtime in waiting_time_individual:
        total_watingtime = total_watingtime + waitingtime

    print(total_watingtime / totalcustomers)


input_details(totalcustomers)
check_best_wait_time(list_ordertime, list_entrytime, totalcustomers)
