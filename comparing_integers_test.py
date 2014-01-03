import unittest
from comparing_integers import compare_ints

class test_compare_ints_function(unittest.TestCase):

  def test_equal_integers(self):
    self.assertEqual(compare_ints(2,2), True)

  def test_unequal_integerts(self):
    self.assertEqual(compare_ints(2,3), False)

  def test_zero_comparision(self):
    self.assertEqual(compare_ints(2,0), False)