import unittest

from scripts.intermediate import PNR_Status


class TestPNRStatus(unittest.TestCase):

    def testPNRStatusPositive(self):
        self.assertAlmostEqual(PNR_Status.pnrstatus(2136892484), 200)

    def test_PNR_Status_Failed(self): # naming convention pep - 8
        self.assertRaises(TypeError, PNR_Status.pnrstatus("123456"))

    def testPNRStatusFailedNegitive(self):
        self.assertRaises(TypeError, PNR_Status.pnrstatus(-12345))
