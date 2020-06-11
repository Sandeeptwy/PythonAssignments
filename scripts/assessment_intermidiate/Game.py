s = input("Enter a string in capital\n")

vowels = ['A', 'E', 'I', 'O', 'U']

dis = {}
dis2 = {}


def game_fun_consonants(s):
    i = 1
    j = 0
    k = len(s)
    while j < len(s):
        while k > 0:
            if s[j] in vowels:
                k = k - 1
                continue
            else:
                list2 = []
                t = j
                for a in range(k):
                    list2.append(s[t])
                    t = t + 1
                if str(list2) in dis:
                    point2 = dis.get(str(list2))
                    dis[str(list2)] = point2 + 1
                    k = k - 1
                    continue
                else:
                    dis[str(list2)] = 1
                list2.clear()
            k = k - 1
        j = j + 1
        k = len(s) - i
        i = i + 1


def game_fun_vowels(s):
    i = 1
    j = 0
    k = len(s)
    while j < len(s):
        while k > 0:
            if s[j] not in vowels:
                k = k - 1
                continue
            else:
                list2 = []
                t = j
                for a in range(k):
                    list2.append(s[t])
                    t = t + 1
                if str(list2) in dis2:
                    point2 = dis2.get(str(list2))
                    dis2[str(list2)] = point2 + 1
                    k = k - 1
                    continue
                else:
                    dis2[str(list2)] = 1
                list2.clear()
            k = k - 1
        j = j + 1
        k = len(s) - i
        i = i + 1


game_fun_consonants(s)
game_fun_vowels(s)

print(dis)
print(dis2)

a = 0
for b in dis.values():
    a = a + b
print("Total Points gain by consonants: " + str(a))
a1 = 0
for b in dis2.values():
    a1 = a1 + b
print("Total Points gain by vowels: " + str(a1))
