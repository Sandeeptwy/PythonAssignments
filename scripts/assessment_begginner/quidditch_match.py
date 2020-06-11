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
    i = i + 1

print(list1)

# o/p:
# ['(G4)', '(S2)', '(H3)', '(G2)', '(R5)', '(S3)', '(H5)']
