import unittest
from binary_search_tree import Tree

class test_binary_search_tree_implementation(unittest.TestCase):

  def test_one_node_tree(self):
    t = Tree()
    t.add(23)
    self.assertEqual(t.root.value, 23)

  def test_three_node_tree(self):
    '''
    this sample tree should look like:
        23
        /\ 
      15  47
    '''
    t = Tree()
    t.add(23)
    t.add(15)
    t.add(47)
    self.assertEqual(t.root.value, 23)
    self.assertIsNotNone(t.root.left)
    self.assertIsNotNone(t.root.right)
    self.assertEqual(t.root.left.value, 15)
    self.assertEqual(t.root.right.value, 47)

  def test_4_node_right_tree(self):
    '''
    another sample tree, this one with only right nodes
    13 \ 14 \ 15
    '''
    t = Tree()
    t.add(13)
    t.add(14)
    t.add(15)
    self.assertIsNone(t.root.left)
    self.assertEqual(t.root.value, 13)
    self.assertEqual(t.root.right.value, 14)
    self.assertEqual(t.root.right.right.value, 15)
