import unittest
#from first_non_repeat import first_non_repeat
from first_non_repeat import first_non_repeat_using_count as first_non_repeat

# there are two different implementations first_non_repeat and first_non_repeat_using_count
# comment out one of the imports above to test either implementation

class test_first_non_repeat_implementation(unittest.TestCase):

  def test_simple_case(self):
    '''
    test a simple case of a word with a first non repeat char
    '''
    word = 'total'
    self.assertEqual(first_non_repeat(word), 'o')

  def test_false_case(self):
    '''
    test a case where a word has no non-repeated characters
    '''
    word = 'papa'
    self.assertFalse(first_non_repeat(word))

  def test_tail_case(self):
    '''
    test a case where the first repeated character is the very last one
    '''
    word = 'pappas'
    self.assertEqual(first_non_repeat(word), 's')

  def test_single_character_case(self):
    '''
    test a string with only one character
    '''
    word = 'a'
    self.assertEqual(first_non_repeat(word), 'a')