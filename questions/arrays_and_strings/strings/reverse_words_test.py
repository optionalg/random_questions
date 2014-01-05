import unittest
from reverse_words import reverse_words

class test_reverse_words_implementation(unittest.TestCase):

  def test_simple_case(self):
    '''
    test a simple three word sentence
    '''
    sentence = "Hello, good day!"
    expected = "day! good Hello,"
    self.assertEqual(reverse_words(sentence), expected)

  def test_case_where_nothing_changes(self):
    '''
    test a one-word sentence where a reversal of words should do nothing
    '''
    sentence = "Hello"
    expected = sentence
    self.assertEqual(reverse_words(sentence), expected)

  def test_a_longer_sentence(self):
    '''
    test a multi-word sentence
    '''
    sentence = 'Hello my name is Dolly and I would like to be your friend'
    expected = 'friend your be to like would I and Dolly is name my Hello'
    self.assertEqual(reverse_words(sentence), expected)

