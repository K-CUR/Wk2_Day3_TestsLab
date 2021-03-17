import unittest
from src.drinks import Drink

class TestDrink(unittest.TestCase):
    # brackets > inside this class I want to grab some methods and code availble as part of the unittest
    # pass

    def setUp(self):
        # setUp must be written with capital U
        self.drink = Drink("Jack and coke", 5.00)

    def test_drink_name(self):
        self.assertEqual("Jack and coke", self.drink.name)

    def test_drink_price(self):
        self.assertEqual(5.00, self.drink.price)