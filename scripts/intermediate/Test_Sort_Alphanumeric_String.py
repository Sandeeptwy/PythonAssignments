import unittest

from scripts.intermediate import Sort_Alphanumeric_String


class Alphanumeric(unittest.TestCase):

    def testSortAlphaNumericString(self):
        s = list('A1a1S4')
        self.assertTrue(Sort_Alphanumeric_String.sortString(s))

    def testSortAlphaNumericStringFailed(self):
        s = 'A1a1S4'
        self.assertFalse(Sort_Alphanumeric_String.sortString(s))
