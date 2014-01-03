import unittest
from factorial import factorial_while, factorial_recursion

class test_factorial(unittest.TestCase):

  def test_factorial_while_is_working(self):
    '''
    make sure that 4! = 24 for the while loop implementation
    '''
    self.assertEqual(factorial_while(4), 24)

  def test_factorial_recursion_is_working(self):
    '''
    make sure that 4! = 24 for the recursion implementation
    '''
    self.assertEqual(factorial_recursion(4), 24)

  def test_the_zero_case(self):
    '''
    make sure that both implementations accurately report that 0! = 1
    '''
    self.assertEqual(factorial_recursion(0), 1)
    self.assertEqual(factorial_while(0), 1)

  def test_negative_case(self):
    '''
    make sure that a negative case evaluates to false
    '''
    self.assertFalse(factorial_recursion(-3))
    self.assertFalse(factorial_while(-3))

  def test_the_one_case(self):
    '''
    make sure than 1! = 1
    '''
    self.assertEqual(factorial_while(1), 1)
    self.assertEqual(factorial_recursion(1), 1)