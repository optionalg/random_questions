import unittest
from queue import Queue

class test_queue_implementation(unittest.TestCase):

  def test_first_elemnt_of_queue(self):
    '''
    test that after initial enqueue, the head of the Queue is correct
    '''
    q = Queue()
    q.enqueue(3)
    self.assertEqual(q.head, q.tail)
    self.assertEqual(q.head.value, 3)

  def test_enqueue_then_dequeue(self):
    '''
    test that after an enqueue a dequeue gives what is expected
    '''
    q = Queue()
    q.enqueue(3)
    result = q.dequeue()
    self.assertEqual(result, 3)
    self.assertIsNone(q.head)

  def test_multiple_enqueues(self):
    '''
    test the Queue after multiple enqueues
    '''
    q = Queue()
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    self.assertEqual(q.head.value, 3)
    self.assertEqual(q.tail.value, 5)

  def test_queue_clear(self):
    '''
    test the clear() method
    '''
    q = Queue()
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(13)
    q.clear()
    self.assertIsNone(q.head)
    self.assertIsNone(q.tail)