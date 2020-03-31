import re

PATTERN = '^([456][0-9]{3})-?([0-9]{4})-?([0-9]{4})-?([0-9]{4})$'


def is_valid_card_number(val):
    match = re.match(PATTERN, val)

    if match is None:
        print("Invalid credit card number")
    else:
        print("Valid credit card number")