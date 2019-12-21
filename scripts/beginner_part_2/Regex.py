import re

def checkRegex():
    try:
        re.compile(value)
        return True
    except re.error:
        return "Not a Regex String."

value = input("Enter input to check it is regex or not")
print(checkRegex())