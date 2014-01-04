class tree():
  def __init__(self, data=None, left=None, right=None):
    self.value = data
    self.left = left
    self.right = right

def height(tree):
  '''
  finds the height of a binary tree recursively
  '''
  if tree is None:
    # there is no height of a non-existant tree!
    return 0
  else:
    return 1 + max(height(tree.left), height(tree.right))