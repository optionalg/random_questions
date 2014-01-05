import unittest
from delete_characters import delete_characters

class test_implementation_of_delete_characters(unittest.TestCase):

  def test_one_characater_case(self):
    '''
    make sure that only one character is deleted from string
    '''
    word = 'Happy Birthday'
    delete_this = 'a'
    expected = 'Hppy Birthdy'
    self.assertEqual(delete_characters(word, delete_this), expected)

  def test_do_nothing_case(self):
    '''
    try to delete a character that doesn't exist in the string
    '''
    word = "Happy"
    delete_this = 'z'
    expected = word
    self.assertEqual(delete_characters(word, delete_this), expected)

  def test_multiple_characters_to_delete_case(self):
    '''
    try to delete more than 1 character at a time from the word
    '''
    word = "Happy"
    delete_this = 'ap'
    expected = "Hy"
    self.assertEqual(delete_characters(word, delete_this), expected)

  def test_case_where_result_is_emply(self):
    '''
    try to delete more than 1 character if after the first delete theres nothing left
    '''
    word = "a"
    delete_this = 'ap'
    expected = ''
    self.assertEqual(delete_characters(word, delete_this), expected)


