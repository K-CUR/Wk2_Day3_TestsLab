import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    # brackets > inside this class I want to grab some methods and code availble as part of the unittest
    # pass

    def setUp(self):
        # setUp must be written with capital U
        self.customer = Customer("Paul", 20.00)

    def test_customer_has_name(self):
        self.assertEqual("Paul", self.customer.name)

    def test_customer_has_wallet(self):
        self.assertEqual(20.00, self.customer.wallet)

    def test_customer_reduced_wallet(self):
        self.customer.reduce_wallet(5.00)
        self.assertEqual(15.00, self.customer.wallet)