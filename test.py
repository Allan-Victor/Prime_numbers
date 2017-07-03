import unittest
from Prime.py import num_is_Prime
class Testprimenumber(unittest.TestCase):
    def setUp(self):
        self.num = num_is_Prime()

    def test_number_greater_than_One(self):
        self.assertTrue(is self.num>1)

    def test_number_postive(self):
        self.assertTrue(is self.num>0)

    def test_number_is_integer(self):
        self.assertRaises(ValueError)
        
