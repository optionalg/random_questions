# implement a method on a singly linked list which returns the 
# m-th to last element of that list traversing the list only once

class node():
  def __init__(self, data=None, next=None):
    self.data = data
    self.next = next

class linked_list():
  def __init__(self):
    self.head = None

  def insert(self, data):
    '''
    insert data to the head of list, update head, and return True
    return False if no data is given
    '''
    if data == None:
      return False
    else:
      new_node = node(data = data, next = self.head)
      self.head = new_node

  def mth_to_last(self, m):
    '''
    traverse the current linked list and return the m-th to last
    element of the list if it exists. If list is not long enough
    return None
    '''
    n = 1
    n_node = self.head
    m_node = None
    while n_node:
      n_node = n_node.next
      if n == m: # after traversing m-elements, the m-th to last element is the head
        m_node = self.head
      if n > m:
        m_node = m_node.next
      n += 1
    return m_node
