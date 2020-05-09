anagram = 'Listen'


def anagramWord(word):
    if value == "SILENT":
        print("Congrats you got it right")
        return True
    else:
        print("You have " + str(x) + " no. of attempst left")
        return False


for x in range(3, 0, -1):
    value = input("Guess the Anagram: " + anagram + "\n")
    if anagramWord(value):
        pass
    else:
        print("Try Again")
