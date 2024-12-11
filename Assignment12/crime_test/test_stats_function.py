import unittest
import crime_test
import pandas as pd
from stats_function import calculate_mean_median 

class TestStatsFunction(unittest.TestCase):
    def test_mean_median(self):
        data = pd.DataFrame({'Vict age': [10, 20, 30, 40]})
        mean, median = calculate_mean_median(data)
        self.assertEqual(mean, 25)
        self.assertEqual(median, 25)
    
    def test_empty_vict_age(self):
        data = pd.DataFrame({'Vict age': []})
        with self.assertRaises(ValueError):
            calculate_mean_median(data)

    def test_none_value(self):
        data = pd.DataFrame({'Vict age': [None, None]})
        with self.assertRaises(ValueError):
            calculate_mean_median(data)
