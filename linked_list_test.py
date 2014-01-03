import unittest
from linked_list import linked_list

class test_linked_list_implementation(unittest.TestCase):

  def test_linked_list_initialization(self):
    ll = linked_list()
    self.assertIsNotNone(ll.head)
    self.assertIsNone(ll.tail)

  def test_first_insert_method(self):
    '''
    when first insert is called, head and tail should equal
    and the data stored in head should be equal to the data inserted
    '''
    ll = linked_list()
    d = 'arbitrary data'
    ll.insert(d) #insert arbitrary data into the list
    self.assertEqual(ll.head, ll.tail)
    self.assertEqual(ll.head.data, d)

  def test_second_insert(self):
    '''
    after the second insert, the head should point to the tail
    '''
    ll = linked_list()
    first_datum = 'the first bit of arbitrary data'
    second_datum = 'the second bit of arbitrary data'
    ll.insert(first_datum)
    ll.insert(second_datum)
    # head.next should point to tail
    self.assertEqual(ll.head.next, ll.tail)
    # head.data should be the last data inserted, tail should be first
    self.assertEqual(ll.head.data, second_datum)
    self.assertEqual(ll.head.next.data, first_datum)

  def test_view_all_method(self):
    '''
    make sure the view_all method returns a list of all data in the correct order
    '''
    ll = linked_list()
    first_datum = 'first'
    second_datum = 'second'
    third_datum = 'third'
    ll.insert(first_datum)
    ll.insert(second_datum)
    ll.insert(third_datum)
    self.assertEqual(ll.view_all(), [third_datum, second_datum, first_datum])

