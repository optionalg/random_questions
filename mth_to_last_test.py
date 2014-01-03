import unittest
from mth_to_last import linked_list

class test_mth_to_last_implementation(unittest.TestCase):

  def test_linked_list_inserts_correctly(self):
    ll = linked_list()
    ll.insert('hello world')
    self.assertEqual(ll.head.data, 'hello world')

  def test_simple_case(self):
    ll = linked_list()
    ll.insert('last, aka tail')
    ll.insert('second to last')
    ll.insert('third to last')
    ll.insert('fourth to last')
    ll.insert('fifth to last')
    self.assertEqual(ll.mth_to_last(4).data, 'fourth to last')

  def test_not_long_enough_case(self):
    ll = linked_list()
    ll.insert('last')
    ll.insert('second to last')
    self.assertIsNone(ll.mth_to_last(5))

  def test_just_long_enough_case(self):
    ll = linked_list()
    ll.insert('last')
    ll.insert('second to last')
    ll.insert('third_to_last')
    self.assertEqual(ll.mth_to_last(3).data, 'third_to_last')
