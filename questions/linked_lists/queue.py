class Node():
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

class Queue():
  def __init__(self):
    self.head = None
    self.tail = None

  def enqueue(self, value):
    '''
    create a new node, place it after the tail
    '''
    new_node = Node(value) # create a new Node
    if self.tail:
      self.tail.next = new_node
    self.tail = new_node

    if not self.head:
      self.head = new_node

    return True

  def dequeue(self):
    '''
    remove head of the queue and return it, or return False is head is None
    '''
    if self.head:
      node = self.head
      self.head = node.next
      return node.value
    else:
      return False

  def clear(self):
    self.head = None
    self.tail = None