from stack import Stack

def preorder_traversal(tree, data = []):
  '''
  traverse the tree: node first, then left, then right
  '''
  if tree is None:
    # if tree is None there is nothing to add to the traversal
    return data
  else:
    # if tree is not None, return the root value, then traverse the left first, then the right
    data.append(tree.value)
    data = preorder_traversal(tree.left, data)
    data = preorder_traversal(tree.right, data)
    return data

def inorder_traversal(tree, data=[]):
  '''
  traverse the tree: left first, then node, then right
  '''
  if tree is None:
    return data
  else:
    data = inorder_traversal(tree.left, data)
    data.append(tree.value)
    data = inorder_traversal(tree.right, data)
    return data

def postorder_traversal(tree, data=[]):
  '''
  traverse the tree: left first, then right, then node
  '''
  if tree is None:
    return data
  else:
    data = postorder_traversal(tree.left, data)
    data = postorder_traversal(tree.right, data)
    data.append(tree.value)
    return data

def preorder_traversal_no_recursion(node):
  '''
  perform a preorder traversal without using recursion
  in this case, use a stack and push nodes to stack in order
  '''
  data = []
  s = Stack()
  while node:
    data.append(node.value)
    if node.right:
      s.push(node.right)
    if node.left:
      s.push(node.left)
    node = s.pop()
  return data
