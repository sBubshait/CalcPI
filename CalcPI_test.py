from CalcPI import CalcPI
import unittest

# Testing values were taken from: https://mathshistory.st-andrews.ac.uk/HistTopics/1000_places/

class CalcPITesting(unittest.TestCase):
    def test_correctUpTo(self):
        self.assertEqual(CalcPI.correctUpTo(1)[0: 1 + 2], "3.1")
        self.assertEqual(CalcPI.correctUpTo(5)[0: 5 + 2], "3.14159")
        self.assertEqual(CalcPI.correctUpTo(10)[0: 10 + 2], "3.1415926535")
        self.assertEqual(CalcPI.correctUpTo(100)[0: 100 + 2], "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679")
        self.assertEqual(CalcPI.correctUpTo(144)[0: 144 + 2], "3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359")

    def test_check(self):
        self.assertEqual(CalcPI.check("4.1"), "Correct up to -2 digits!")
        self.assertEqual(CalcPI.check("3.4334"), "Correct up to 0 digits!")
        self.assertEqual(CalcPI.check("3.14159"), "Matched all 5 digits!")
        self.assertEqual(CalcPI.check("3.14159000"), "Correct up to 5 digits!")
        self.assertEqual(CalcPI.check("3.1415926535"), "Matched all 10 digits!")
        self.assertEqual(CalcPI.check("3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"), "Matched all 100 digits!")
        self.assertEqual(CalcPI.check("3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359"), "Matched all 144 digits!")

if __name__ == '__main__':
    unittest.main()