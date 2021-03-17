import unittest
from src.pub import Pub
from src.drinks import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    # brackets > inside this class I want to grab some methods and code availble as part of the unittest
    # pass

    def setUp(self):
        # setUp must be written with capital U
        self.pub = Pub("The Prancing Pony", 100.00)
    # we're going to have a test at a Pub class and it's going to have a name and an amount

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
    # it doesn't always have to be assertEqual, there are others like assertFalse
    
    def test_sell_drink(self):
        customer = Customer("Paul", 20.00)
        drink = Drink("Jack and coke", 5.00)
        self.pub.sell_drink(drink, customer)
        self.assertEqual(15, customer.wallet)
        self.assertEqual(105.00, self.pub.till)







