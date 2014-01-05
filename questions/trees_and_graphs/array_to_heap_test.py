import unittest
from array_to_heap import heapify, Node


class test_implementation_of_heapify(unittest.TestCase):

  def test_first_element_becomes_root(self):
    '''
    test that after heapify, the first element of the array has become the tree root
    '''
    a = [Node(5), Node(4)]
    a = heapify(a)
    self.assertIsNotNone(a.root)
    self.assertEqual(a.root.value, 5)

  def test_with_sorted_array(self):
    '''
    test that, when given an array of sorted nodes, the output is a max_heap,
    in this case an array of nodes that looks like [5,4,3] should be turned into
    a Tree which looks like:
        5
       / \ 
      4   3
    '''
    a = [Node(5), Node(4), Node(3)]
    a = heapify(a)
    self.assertEqual(a.root.value, 5)
    self.assertEqual(a.root.left.value, 4)
    self.assertEqual(a.root.right.value, 3)

