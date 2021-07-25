class Empty(Exception):
  pass

class _DoublyLinkedBase:
  """Base class for doubly linked lists."""

  class _DNode:
    """Create a Node compatible with a doubly linked list."""

    def __init__(self, val, next=None, prev=None):
      self._val=val
      self._next=next
      self._prev=prev

  def __init__(self):
    """Define sentinels."""
    self._header=self._DNode(None, None, None)
    self._trailer=self._DNode(None, None, None)
    self._header._next=self._trailer
    self._trailer._prev=self._header
    self._size=0

  def is_empty(self):
    """Return True if the primary is empty."""
    return self._size==0

  def __len__(self):
    """Return the length of the primary sequence (primary sequence is sequence of Nodes excluding sentinels)."""
    return self._size

  def _insert_between(self, e, predecessor, successor):
    """Insert a DNode e between successor and predecessor."""
    new_node=self._DNode(e,successor, predecessor)
    successor._prev = new_node
    predecessor._next = new_node
    self._size+=1
    return new_node

  def _delete_node(self, node):
    """Remove a DNode and return its value."""
    if self.is_empty():
      raise Empty("List is empty.")
    successor=node._next
    predecessor=node._prev
    answer=node._val
    successor._prev=predecessor
    predecessor._next=successor
    self._size-=1
    return answer
