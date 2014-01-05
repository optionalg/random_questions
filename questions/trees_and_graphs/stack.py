# simple stack implementation based on previous efforts (for use with tree searches)

class Node():
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

class Stack():
  def __init__(self):
    self.head = None

  def push(self, value):
    if not value:
      return False
    else:
      new_node = Node(value, next = self.head)
      self.head = new_node
      return True

  def pop(self):
    if not self.head:
      return False
    else:
      node = self.head
      self.head = node.next
      return node.value

  def clear(self):
    self.head = None
    return True
