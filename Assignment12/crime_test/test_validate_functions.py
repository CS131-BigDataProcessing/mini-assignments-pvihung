import unittest
import crime_test
import pandas as pd
from validate_functions import validate_vict_sex, validate_vict_age

class TestValidateFunctions(unittest.TestCase):
    def test_valid_vict_sex(self):
        # Do trong file validate_functions thi moi cai nay deu store vo 1 gia tri 
        # Nen gio phai goi gia tri roi assertEqual chu khong duoc goi function ra
        
        # Correct value
        # Check cai gi thi assert cai day true/false thi assertTrue/False
        data = pd.DataFrame({'Vict sex': ['M', 'F', 'M', 'F']})
        self.assertTrue(validate_vict_sex(data))

    def test_invalid_vict_sex(self):
        data = pd.DataFrame({'Vict sex': ['M', 'F', None, '']})
        self.assertFalse(validate_vict_sex(data))

    def test_missing_vict_sex(self):
        data = pd.DataFrame({'Vict race' : ['M', 'F', 'F', 'F']})
        with self.assertRaises(ValueError):
            validate_vict_sex(data)

    def test_valid_vict_age(self):
        data = pd.DataFrame({'Vict age': [20, 13, 42, 39]})
        self.assertTrue(validate_vict_age(data))

    def test_invalid_vict_age(self):
        data = pd.DataFrame({'Vict age': [0, 1000, None, -5]})
        self.assertFalse(validate_vict_age(data))

    def test_missing_vict_age(self):
        data = pd.DataFrame({'Vict sex': [25, 34, 70, 30]})
        with self.assertRaises(ValueError):
            validate_vict_age(data)

