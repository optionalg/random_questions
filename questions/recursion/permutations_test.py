import unittest
from permutations import permute

class test_permutations_implementation(unittest.TestCase):

  def test_three_word_case(self):
    '''
    test that when passed HAT the function returns all permutations of HAT (in correct order)
    '''
    string = 'HAT'
    expected = ['HAT', 'HTA', 'AHT', 'ATH', 'THA', 'TAH']
    self.assertEqual(permute(string), expected)
    