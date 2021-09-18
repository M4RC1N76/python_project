import unittest
from models.city import City
from models.country import Country
# Country - name, visited, id
# City - name, visited, id
class TestCity(unittest.TestCase): # wrong name TestWork

    def setUp(self):
        self.country = Country("Italy", False)
        self.city = City("Naples", False) # wrong indentation outwith the function

    def test_city_has_name(self):  # wrong indentation outwith the function
        self.assertEqual("Naples", self.city.name) # wrong indentation outwith the function
