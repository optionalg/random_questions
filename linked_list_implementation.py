# Implement a linked list in Python

class node():
  def __init__(self, data = None, next = None):
    self.data = data
    self.next = next

class linked_list():
  def __init__(self):
    self.head = node()
    self.tail = None

  def insert(self, data):
    if self.tail == None:
      new_node = node(data = data, next = None)
      self.tail = new_node
    else:
      new_node = node(data = data, next = self.head)
    self.head = new_node
