s = int(input("Enter the # of customer details\n"))

list = []
list_time = []
l = s
while l > 0:
    i = input(
        "Enter the details of customers in follwing format ""2 5"", here 2 will be the time customer entered the Restaurant and 5 is the time required to make the order\n")
    if i[1] != ' ':
        print("Wrong format Re-Enter")
        i = input(
            "Enter the details of customers in follwing format ""2 5"", here 2 will be the time customer entered the Restaurant and 5 is the time required to make the order\n")

    list.append(i[0])
    list_time.append(i[2])
    l = l - 1


def check_best_wait_time(list, list_time, s):
    c1 = list
    c2 = []

    dic = {}
    for a in range(s):
        dic[str(list[a])] = list_time[a]

    print(dic)
    c1.sort()

    b = 0
    for a in c1:
        b = b + int(a)
        c2.append(b)

    l = 0
    for a in c1:
        c2[l] = c2[l] - int(dic.get(str(a)))
        l = l + 1

    print("Waiting Time for each individual ", c2)

    b = 0
    for a in c2:
        b = b + a

    print(b / s)


check_best_wait_time(list, list_time, s)
