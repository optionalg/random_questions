import unittest
from comparing_integers import compare_ints

class test_compare_ints_function(unittest.TestCase):

  def test_equal_integers(self):
    '''make sure that two equal integers are found to be equal'''
    self.assertEqual(compare_ints(2,2), True)

  def test_unequal_integerts(self):
    '''make sure that two unequal integers are found to be unequal'''
    self.assertEqual(compare_ints(2,3), False)

  def test_zero_comparison(self):
    '''make sure that a zero as the second integer doesnt break the function'''
    self.assertEqual(compare_ints(2,0), False)