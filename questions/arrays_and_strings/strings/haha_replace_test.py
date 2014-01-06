import unittest
from haha_replace import haha_replace_function

class test_implementation_of_haha_replace_function(unittest.TestCase):

  def test_simple_case(self):
    '''
    test that a sentence with "the" gets it replaced with "HAHA"
    '''
    sentence = "the world is dark"
    expected = "HAHA world is dark"
    self.assertEqual(haha_replace_function(sentence), expected)

  def test_sentence_with_no_the(self):
    '''
    test that a sentence with no "the" gets nothing replaced
    '''
    sentence = "hello world"
    self.assertEqual(haha_replace_function(sentence), sentence)