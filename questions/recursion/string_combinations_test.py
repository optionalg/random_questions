import unittest
from string_combinations import combinate

class test_string_combinations_implementation(unittest.TestCase):
  '''
  test the implementation of the combinate function from the string_combinations.py file
  '''

  def test_three_letter_case(self):
    '''
    test the combinate function using a simple three letter string
    '''
    string = '123'
    expected = ['1', '12', '123', '13', '2', '23', '3']
    self.assertEqual(combinate(string), expected)