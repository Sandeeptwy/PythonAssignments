predefined = 'T'
value = input("Guess a charater: \n")


def checkCharacter(char):
    if char.upper() == predefined.upper():
        print("Congrats you correctly guessed the predefined alphabet: " + predefined)
    else:
        raise Exception("Entered Alphabet is different than the predefined number")


checkCharacter(value)
