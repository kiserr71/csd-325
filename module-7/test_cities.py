#Robert Kiser
#07/12/25
#CSD325
#Module 7.2 Assignment

import unittest
from city_functions import country_format

class test_string_methods(unittest.TestCase):

    def test_city_country(self):
        formatted_city = country_format('chile', 'santiago')
        self.assertEqual(formatted_city, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()
