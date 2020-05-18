def sortString(s):
    if type(s) not in [list]:
        return False
    else:
        try:
            is_sorted = False

            while not is_sorted:
                for i in range(len(s) - 1, 0, -1):

                    if s[i] > s[i - 1]:
                        print("output: ", i, s[i], s[i - 1])
                        s[i - 1], s[i] = s[i], s[i - 1]
                        break
                else:
                    is_sorted = True
            print("".join(s))
            return True

        except Exception as e:
            return False


s = list('A1a1S4')
print(sortString(s))
