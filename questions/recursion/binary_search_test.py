import unittest
from binary_search import binary_search

class test_binary_search_implementation(unittest.TestCase):

  def test_simple_case(self):
    '''
    test that the binary search returns the correct index of an integer
    in a sorted list
    '''
    a = [1,2,3,4,5,6,7,8,9]
    focus = 3
    expected_index = 2
    self.assertEqual(binary_search(a, focus), expected_index)

  def test_case_of_multiple_values(self):
    '''
    test that the binary search returns the correct inedex of an integer
    in a sorted list with repeated values
    '''
    a = [11, 12, 12, 12, 13, 14, 15, 16, 17, 17, 18, 29, 30]
    focus = 13
    expected_index = 4
    self.assertEqual(binary_search(a, focus), expected_index)

