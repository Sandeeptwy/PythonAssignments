from itertools import permutations
from itertools import combinations

# use functions

length_string = int(input("Enter the length of a string b/w 1 and 10\n"))

string = []


def input_from_user(length_string):
    while 1 == 1:
        if length_string > 10 or length_string < 1:
            print("Wrong input, Enter the length of a string b/w 1 and 10")
            length_string = int(input("Enter the length of a string b/w 1 and 10\n"))
            continue
        else:
            break

    # l = length_string

    entered_string = input(
        "Enter the string space separated in lower case\n")
    while 1 == 1:
        if entered_string[1] != ' ' or entered_string[0] == ' ' or len(entered_string) != length_string * 2 - 1:
            print("Wrong format or length doesn't match. Re-Enter")
            entered_string = input(
                "Enter the string space separated in lower case\n")
            continue
        else:
            for character in entered_string:
                if character == ' ':
                    continue
                else:
                    string.append(character)
            break


def enter_indices(length_string, indices):
    while 1 == 1:
        if indices > length_string or indices < 1:
            print("Index should be between ", length_string, " and 1")
            indices = int(input("Enter the indices\n"))
            continue
        else:
            break


def check_probablity(string, indices):
    perm = combinations(string, indices)
    count = 0
    size = 0
    for characters in perm:
        if 'a' in characters:
            count = count + 1
        size = size + 1
        print(characters)
    print(count, size)
    print(count / size)


input_from_user(length_string)
indices = int(input("Enter the indices\n"))
enter_indices(length_string, indices)
check_probablity(string, indices)
