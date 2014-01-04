class tree():
  def __init__(self, data=None, left=None, right=None):
    self.value = data
    self.left = left
    self.right = right


def height_of_tree(tree):
  if not tree.left and not tree.right:
    return 1
  else:
    return 1 + max(height_of_tree(tree.left), height_of_tree(tree.right))