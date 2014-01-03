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
    '''
    insert new data into the list and update the head
    '''
    if self.tail == None:
      # the tail is none only on the first insert, so save that as the tail
      new_node = node(data = data, next = None)
      self.tail = new_node
    else:
      new_node = node(data = data, next = self.head)
    self.head = new_node

  def view_all(self):
    '''
    return a list object of all the data in order (first to last)
    '''
    view = []
    node = self.head
    while node:
      view.append(node.data)
      node = node.next
    return view