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

  def height(self, tree=None, root=True):
    '''
    returns the height of the tree, recursively
    ''' 
    if root:
      # only true the first recursion
      tree = self.root

    if tree is None:
      # a none tree has no height!
      return 0
    else:
      # each time around the recursion, the depth increases by 1
      return 1 + max(
        self.height(tree=tree.left, root=False), 
        self.height(tree=tree.right, root=False)
        )

