userString = input("Enter a string in capital\n")

vowels = ['A', 'E', 'I', 'O', 'U']

dict_consonants = {}
dict_vowels = {}


def game_fun_consonants(userstring):
    i = 1
    startingindex = 0
    length = len(userstring)
    while startingindex < len(userstring):
        while length > 0:
            if userstring[startingindex] in vowels:
                length = length - 1
                continue
            else:
                list2 = []
                consonants_index = startingindex
                for a in range(length):
                    list2.append(userstring[consonants_index])
                    consonants_index = consonants_index + 1
                if str(list2) in dict_consonants:
                    point2 = dict_consonants.get(str(list2))
                    dict_consonants[str(list2)] = point2 + 1
                    length = length - 1
                    continue
                else:
                    dict_consonants[str(list2)] = 1
                list2.clear()
            length = length - 1
        startingindex = startingindex + 1
        length = len(userstring) - i
        i = i + 1


def game_fun_vowels(userstring):
    i = 1
    startingindex = 0
    length = len(userstring)
    while startingindex < len(userstring):
        while length > 0:
            if userstring[startingindex] not in vowels:
                length = length - 1
                continue
            else:
                list2 = []
                vowels_index = startingindex
                for a in range(length):
                    list2.append(userstring[vowels_index])
                    vowels_index = vowels_index + 1
                if str(list2) in dict_vowels:
                    point2 = dict_vowels.get(str(list2))
                    dict_vowels[str(list2)] = point2 + 1
                    length = length - 1
                    continue
                else:
                    dict_vowels[str(list2)] = 1
                list2.clear()
            length = length - 1
        startingindex = startingindex + 1
        length = len(userstring) - i
        i = i + 1


def show_points():
    index_consonants = 0
    for consonant_point in dict_consonants.values():
        index_consonants = index_consonants + consonant_point
    print("Total Points gain by consonants: " + str(index_consonants))
    index_vowels = 0
    for vowels_point in dict_vowels.values():
        index_vowels = index_vowels + vowels_point
    print("Total Points gain by vowels: " + str(index_vowels))


game_fun_consonants(userString)
game_fun_vowels(userString)

print(dict_consonants)
print(dict_vowels)

show_points()
