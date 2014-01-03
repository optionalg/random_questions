import unittest
from stack import stack

class test_stack_implementation(unittest.TestCase):

  def test_stack_initialization(self):
    '''
    make sure a new stack is not None!
    '''
    new_stack = stack()
    self.assertIsNotNone(new_stack)

  def test_push_method(self):
    '''
    make sure the push method works as it should
    '''
    data = 'some bit of artbitrary data'
    new_stack = stack()
    self.assertTrue(new_stack.push(data))
    self.assertEqual(new_stack.head.data, data)

  def test_pop_on_empty_stack(self):
    '''
    stack.pop() on an empty stack should return False
    '''
    new_stack = stack()
    self.assertFalse(new_stack.pop())

  def test_push_then_pop(self):
    '''
    push a value, then pop it. Data in should be correct, and result stack should
    not be poppable
    '''
    new_stack = stack()
    data = 'some bit of arbitrary data'
    new_stack.push(data)
    self.assertEqual(new_stack.pop(), data)
    self.assertFalse(new_stack.pop())

  def test_push_pop_twice(self):
    '''
    push two values then pop the second. The head should be the first value pushed 
    '''
    new_stack = stack()
    data1 = 'first'
    data2 = 'second'
    new_stack.push(data1)
    new_stack.push(data2)
    new_stack.pop()
    self.assertEqual(new_stack.head.data, data1)

  def test_stack_clear_method(self):
    '''
    push a few values to a new stack, then clear it and test that it is clear
    '''
    new_stack = stack()
    new_stack.push('first data')
    new_stack.push('second_data')
    new_stack.push('third_data')
    new_stack.clear()
    self.assertIsNone(new_stack.head)