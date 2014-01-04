# implement a binary search tree in Python

class Node():
  def __init__(self, value=None):
    self.value = value
    self.left = None
    self.right = None

class Tree():
  def __init__(self):
    self.root = None

  def add(self, value, node=None, root=True):
    '''
    add new values to the tree, recursively
    '''
    if self.root is None:
      self.root = Node(value)
    else:
      if root: # root indicates the first recursion, all others will be False
        node = self.root

      if value < node.value:
        if node.left:
          self.add(value=value, node=node.left, root=False)
        else:
          node.left = Node(value)
      else:
        if node.right:
          self.add(value=value, node=node.right, root=False)
        else:
          node.right = Node(value)

