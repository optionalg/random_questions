import unittest
from height_of_tree import height, tree

class test_height_of_tree_implementation(unittest.TestCase):

  def create_sample_tree(self):
    '''
    create a simple tree with the structure:
        A
       / \ 
      B   C
         / \ 
        D   E
       / \   \ 
      F   G   H
    '''
    root = tree('A', tree('B'), tree('C', tree('D', tree('F'), tree('G')), tree('E', None, tree('H'))))
    return root

  def test_creation_of_simple_tree(self):
    '''
    the simple tree above should be created and return a non-None thing
    '''
    sample_tree = self.create_sample_tree()
    self.assertEqual(sample_tree.value, 'A')
    self.assertEqual(sample_tree.left.value, 'B')
    self.assertEqual(sample_tree.right.value, 'C')

  def test_height_of_tree_function(self):
    '''
    the height of the sample tree above should be equal to 4
    '''
    sample_tree = self.create_sample_tree()
    self.assertEqual(height(sample_tree), 4)