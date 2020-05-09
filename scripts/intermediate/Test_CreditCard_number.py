import unittest

from scripts.intermediate import CreditCard_number


class CreditCard(unittest.TestCase):

    def testCreditCardNumberisValid(self):
        # val = input("Enter your credit card number: (format xxxx-xxxx-xxxx-xxxx)\n")
        val = "4569999999999999"
        self.assertTrue(CreditCard_number.is_valid_card_number(val))

    def testCreditCardNumberisInValid(self):
        val = "123456789"
        self.assertFalse(CreditCard_number.is_valid_card_number(val))

    def testCreditCardNumberisInValidType(self):
        val = "123456789"
        self.assertRaises(TypeError, CreditCard_number.is_valid_card_number(val))
