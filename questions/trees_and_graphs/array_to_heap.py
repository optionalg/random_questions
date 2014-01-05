class Node():
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

class Tree():
  def __init__(self):
    self.root = None

def heapify(array):
  '''
  take in an array and return a heap with underlying architecture as balanced BST
  '''
  n = 0
  heap = Tree()
  heap.root = array[n]
  while 2*n+2 < len(array):
    node = array[n]
    node.left = array[2*n+1]
    node.right = array[2*n+2]
    n += 1 
  return heap