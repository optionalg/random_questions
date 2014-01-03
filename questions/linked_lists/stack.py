# Problem: implement a stack in Python with push(), pop() and clear() methods

class node():
  def __init__(self, data = None, next = None):
    self.data = data
    self.next = next

class stack():
  def __init__(self):
    self.head = None

  def push(self, data):
    '''
    take data, set at head of linked list, return True if successful
    return False if no data is passed
    '''
    if data == None:
      return False
    else:
      new_node = node(data = data, next = self.head)
      self.head = new_node
      return True

  def pop(self):
    '''
    return the value of the current head, set head.next as the new head
    return False if the current head is None
    '''
    if self.head == None:
      return False
    else:
      current_head = self.head
      self.head = current_head.next
      return current_head.data

  def clear(self):
    '''
    set the head value to None, which destroys all links to previous nodes
    '''
    self.head = None
