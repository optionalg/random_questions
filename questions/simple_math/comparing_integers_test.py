import unittest
from comparing_integers import compare_ints_1, compare_ints_2

class test_compare_ints_function(unittest.TestCase):

  def test_equal_integers(self):
    '''make sure that two equal integers are found to be equal'''
    self.assertTrue(compare_ints_1(2,2))
    self.assertTrue(compare_ints_2(2,2))

  def test_unequal_integerts(self):
    '''make sure that two unequal integers are found to be unequal'''
    self.assertFalse(compare_ints_1(2,3))
    self.assertFalse(compare_ints_2(2,3))

  def test_zero_comparison(self):
    '''make sure that a zero as the second integer doesnt break the function'''
    self.assertFalse(compare_ints_1(2,0))
    self.assertFalse(compare_ints_2(2,0))

  def test_both_zeros_comparison(self):
    self.assertTrue(compare_ints_1(0,0))
    self.assertTrue(compare_ints_2(0,0))