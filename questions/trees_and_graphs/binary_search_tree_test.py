import unittest
from binary_search_tree import Tree

class test_binary_search_tree_implementation(unittest.TestCase):

  def test_one_node_tree(self):
    t = Tree()
    t.add(23)
    self.assertEqual(t.root.value, 23)

  def create_three_node_tree(self):
    '''
    create a sample tree which looks like:
        23
        /\ 
      15  47
    '''
    t = Tree()
    t.add(23)
    t.add(15)
    t.add(47)
    return t

  def test_three_node_tree(self):
    '''
    test the three nodes of the tree created in the create_three_node_tree() function
    '''
    t = self.create_three_node_tree()
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

  def test_height_of_zero_node_tree(self):
    '''
    assert that the height of a tree with no nodes should be 0
    '''
    t = Tree()
    self.assertEqual(t.height(), 0)

  def test_height_of_three_node_tree(self):
    '''
    assert that the height of the simple three node tree is indeed 2
    '''
    t = self.create_three_node_tree()
    self.assertEqual(t.height(), 2)

  def test_height_of_known_height_tree(self):
    '''
    assert that the height of a tree known to be 4 is actually 4
    '''
    t = Tree()
    t.add(1)
    t.add(2)
    t.add(3)
    t.add(4)
    self.assertEqual(t.height(), 4)
