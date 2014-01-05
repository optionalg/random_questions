import unittest
from stack import Stack

class test_simple_implementaiton_of_stack(unittest.TestCase):

  def test_stack_push(self):
    '''make sure simple push works'''
    s = Stack()
    self.assertIsNotNone(s)
    s.push(3)
    self.assertEqual(s.head.value, 3)

  def test_stack_push_pop(self):
    '''make sure push then pop works'''
    s = Stack()
    s.push(3)
    result = s.pop()
    self.assertEqual(result, 3)