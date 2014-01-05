import unittest
from binary_search_tree import Tree
from traversal import preorder_traversal, inorder_traversal, postorder_traversal
from traversal import preorder_traversal_no_recursion

class test_traversal_implementations(unittest.TestCase):

  def create_sample_tree(self):
    '''
    create a sample tree to use in the traversal implementations
    '''
    t = Tree()
    t.add(100)
    t.add(50)
    t.add(25)
    t.add(75)
    t.add(150)
    t.add(125)
    t.add(175)
    t.add(110)
    return t.root

  def test_preorder_traversal_implementation(self):
    '''
    test that the output is indeed what is expected
    '''
    t = self.create_sample_tree()
    expected = [100, 50, 25, 75, 150, 125, 110, 175]
    self.assertEqual(preorder_traversal(t), expected)

  def test_inorder_traversal_implementation(self):
    '''
    test that the inorder traversal implementation is what is expected
    '''
    t = self.create_sample_tree()
    expected = [25, 50, 75, 100, 110, 125, 150, 175]
    self.assertEqual(inorder_traversal(t), expected)

  def test_postorder_traversal_implementation(self):
    '''
    test that the postorder traversal implementation is what is expected
    '''
    t = self.create_sample_tree()
    expected = [25, 75, 50, 110, 125, 175, 150, 100]
    self.assertEqual(postorder_traversal(t), expected)

  def test_preorder_traversal_no_recursion_implementation(self):
    '''
    test that the preorder traversal with no recursion implementation is working
    '''
    t = self.create_sample_tree()
    expected = [100, 50, 25, 75, 150, 125, 110, 175]
    self.assertEqual(preorder_traversal_no_recursion(t), expected)


