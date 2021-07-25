from DoublyLinkedBase import _DoublyLinkedBase

class Empty(Exception):
  pass 


class PositionalList(_DoublyLinkedBase):
  """Implement a Positional List using Doubly Linked List."""

  class Position:
    """An abstraction representing the location of a single element."""

    def __init__(self, node, container):
      """Set properties of a Position instance."""
      self._node = node
      self._container=container

    def element(self):
      """Return the element stored at this position."""
      return self._node._val

    def __eq__(self,other):
      """Return True if other represents the same Position."""
      return type(self) is type(other) and self._node is other._node

    def __ne__(self,other):
      """Return True if both represent a different Position."""
      return not (self==other)

#---------------------------------------utility method---------------------
  def _validate(self,p):
    """Validate if p belongs to this container."""
    if not isinstance(p,self.Position):
      raise TypeError("p must be of proper type Position")
    if not p._container==self:
      raise ValueError("p does not belong to this container.")
    if p._node._next is None:
      raise ValueError("p does not exist any longer.")
    return p._node

  def _make_position(self,node):
    """Return position instance for given node (or None if sentinel)."""
    if node is self._header or node is self._trailer:
      return None
    else:
      return self.Position(node,self)

  def first(self):
    """Return the first Position in the list (or None if list is empty.)."""
    return self._make_position(self._header._next)

  def last(self):
    """Return the last Position in the list (or None if list is empty)."""
    return self._make_position(self._trailer._prev)

  def before(self,p):
    """Return the Position before Position p (or None if p is first)."""
    original= self._validate(p)
    return self._make_position(original._prev)

  def after(self,p):
    """Return the Position after Position p (or None if p is last)."""
    original=self._validate(p)
    return self._make_position(original._next)

  def __iter__(self):
    """Generate a forward iteration of the elements of the list."""
    cursor=self.first()
    while cursor:
      yield cursor.element()
      cursor= self.after(cursor)

  def _insert_between(self, e, predecessor, successor):
    """Insert an element between two existing nodes."""
    node = super()._insert_between(e,predecessor, successor)
    return self._make_position(node)

  def add_first(self, e):
    """Insert element e at the front of the list and return new Position."""
    return self._insert_between(e, self._header, self._header._next)

  def add_last(self,e):
    """Insert element e at the end of the list and return new Position."""
    return self._insert_between(e,self._trailer._prev,self._trailer)

  def add_before(self,p,e):
    """Insert element e before Position p and return new Position."""
    original=self._validate(p)
    return self._insert_between(e,original._prev, original)

  def add_after(self,p,e):
    """Insert element e after Position p and return new Position."""
    original=self._validate(p)
    return self._insert_between(e,original, original._next)

  def delete(self,p):
    """Remove and return the element at Position p."""
    original=self._validate(p)
    return self._delete_node(original)

  def delete_last(self):
    """Remove and return the last element in the doubly linked list."""
    if self.is_empty():
      raise Empty("Container is empty.")
    return self._delete_node(self.last()._node)

  def replace(self,p,e):
    """Replace the element at position p with e.
    Return the element formerly at Position p"""
    original=self._validate(p)
    old_value=original._val
    original._val=e
    return old_value

# if __name__=="__main__":
#   Plist=PositionalList()
#   p1=Plist.add_first(4)
#   p2=Plist.add_first(8)
#   p3=Plist.add_after(p2,12)
#   it = iter(Plist)
#   for element in list(it):
#     print(element)
