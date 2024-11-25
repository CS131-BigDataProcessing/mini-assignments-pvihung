import unittest 
#phai from file (math_funtions) import ra cac thuat toan can xai (power va divide)
from math_functions import power, divide
# Rieng trong Unittesting thi phai xai class

class TestMathFucntions(unittest.TestCase):
    def test_power_of_zero(self):
        # Kiem tra xem phep tinh (5^0) co bang dap an de ra khong (1)
        self.assertEqual(power(5, 0), 1)

    def test_power_negative(self):
        # Kiem tra phep tinh ma co the co floating point thi nen xai assertAlmostEqual (0.25 co the bi may tinh hieu la 0.25000000)
        self.assertAlmostEqual(power(2, -2), 0.25)

    def test_zero_power(self):
        self.assertEqual(power(0,3),0)

    def test_divide_by_zero(self):
        # vi da raise of math_functions.py roi nen chi can with assertRaises thi co the print ra cai lenh sai do 
        with self.assertRaises(ValueError):
            divide(10, 0)

    def test_zero_numerator(self):
        self.assertEqual(divide(0, 2), 0)

    def test_negative_numerator(self):
        self.assertEqual(divide(-10,2),-5)

    def test_negative_denominator(self):
        self.assertEqual(divide(10,-2),-5)

    def test_both_negative(self):
        self.assertEqual(divide(-10,-2),5)


