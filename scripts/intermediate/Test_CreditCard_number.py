import unittest
import CreditCard_number


class CreditCard(unittest.TestCase):
    val = input("Enter your credit card number: (format xxxx-xxxx-xxxx-xxxx)\n")
    CreditCard_number.is_valid_card_number(val)

    # is_valid_card_number(val)
