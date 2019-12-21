open_list = ["[", "{", "(", "<"]
close_list = ["]", "}", ")", ">"]


def check(myStr):
    stack = []
    for i in myStr:
        if i in open_list:
            stack.append(i)
        elif i in close_list:
            if len(stack) > 0:
                position = close_list.index(i)
                openchar = open_list[position]
                print(position, openchar)

                if openchar in stack:
                    stack.remove(openchar)
                    print(stack)
                else:
                    return "Unbalanced"
            else:
                return "Unbalanced"

    if len(stack) == 0:
        return "Balanced"
    else:
        return  "Unbalanced"


string = "{[{]()<}>}"
print(string, "-", check(string))
