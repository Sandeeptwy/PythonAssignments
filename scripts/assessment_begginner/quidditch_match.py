group = ["G", "G", "G", "G", "S", "S", "H", "H", "H", "G", "G", "R", "R", "R", "R", "R", "S", "S", "S", "H", "H", "H",
         "H", "H"]

length = len(group)
print(length)

i = 1
count = 1

list1 = []
for number in group:
    if i < length:
        if group[i] == group[i - 1]:
            count = count + 1
            pass
        else:
            print(group[i - 1], count)
            list1.append("(" + group[i - 1] + "" + str(count) + ")")
            count = 1
    else:
        print(group[i - 1], count)
        list1.append("(" + group[i - 1] + "" + str(count) + ")")

    # print(i, number)
    i = i + 1

print(list1)

# [(G,4), (S,2), (H,3), (G,2), (R,5), (S,3), (H,5)]
