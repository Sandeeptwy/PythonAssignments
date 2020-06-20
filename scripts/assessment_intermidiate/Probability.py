from itertools import permutations
from itertools import combinations

s = int(input("Enter the length of a string b/w 1 and 10\n"))
while 1 == 1:
    if s > 10 or s < 1:
        print("Enter the length of a string b/w 1 and 10")
        s = int(input("Enter the # of customer details\n"))
        continue
    else:
        break

string = []
l = s

i = input(
    "Enter the string space separated in lower case\n")
while 1 == 1:

    if i[1] != ' ' or i[0] == ' ' or len(i) != s * 2 - 1:
        print("Wrong format or length doesn't match. Re-Enter")
        i = input(
            "Enter the string space separated in lower case\n")
        continue
    else:
        for b in i:
            if b == ' ':
                continue
            else:
                string.append(b)
        break

a = int(input("Enter the indices\n"))

while 1 == 1:
    if a > s or a < 1:
        print("Index should be between ", s, " and 1")
        a = int(input("Enter the indices\n"))
        continue
    else:
        break


def check_probablity(string, a):
    perm = combinations(string, a)
    count = 0
    size = 0
    for i in perm:
        if 'a' in i:
            count = count + 1
        size = size + 1
        print(i)
    print(count, size)
    print(count / size)


print(list)

check_probablity(string, a)
