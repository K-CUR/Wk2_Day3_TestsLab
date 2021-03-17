import unittest
# this is the file that is used to run our program 

from tests.pub_tests import TestPub
from tests.customer_tests import TestCustomer
from tests.drinks_tests import TestDrink
# main (below) will search any imported files (above) for a test class we have set up (in pub_tests.py)
if __name__ == "__main__":
# we want to make sure that unittest is going to run this file (run_test.py)
# referred to as main here
    unittest.main()


