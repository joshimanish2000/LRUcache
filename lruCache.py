#!/usr/bin/env python3

from PositionalListADT import PositionalList

class LRUcache(PositionalList):
  """Implement an LRUcache using a Positional List and a dictionary."""
  
  def __init__(self,max_size=1):
    """Create an empty cache of size max_size."""
    self._max_size = max_size 
    self._pos_dict = dict()  #dictionary that keeps the locations of  #entities in the cache.
    self._Plist = PositionalList()  #Positional list object.
    self._n = 0  #number of entities in the cache 

  def remove_page(self,pos):
    """Remove a page from the Positional Linked List."""
    return self._Plist.delete(pos)

  def move_top(self,page_val):
    """Move a page to the top of the cache."""
    return self._Plist.add_first(page_val)   #returns position of the top page

  def get_page(self,name):
    """Return page 'name' from the cache. Return None if does not exist."""
    try:
      pos = self._pos_dict[name] 
    except KeyError:
      raise KeyError("Page is not in the cache.")
    page_val = self.remove_page(pos)    #remove the page from its  current location
    p_top = self.move_top(page_val)    #insert the page at the top of the cache
    return p_top.element()
  
  def insert_new_page(self,name,e):
    """Insert page e at the top of the cache."""
    #if the cache is full 
    if self._n == self._max_size:
      self._Plist.delete_last()  #first, evict the least rececntly used page
    #if there is space
    p = self._Plist.add_first(e)  #simply insert at the top
    self._pos_dict[name] = p
    self._n+=1

  def __iter__(self):
    """Return iteration of the object."""
    return iter(self._Plist)
  

# if __name__=="__main__":
#   cache = LRUcache(max_size=4)
#   cache.insert_new_page("NASA","nasa.gov")
#   cache.insert_new_page("Wikipedia/United States","wikipedia.org")
#   cache.insert_new_page("Linux","linux.org")
#   cache.insert_new_page("Stack Overflow","stackoverflow.com")
#   print(cache.get_page("NASA"))
#   cache.insert_new_page("United Nations","un.org")
  
#   it = iter(cache)
#   for page in list(it):
#     print(page)
  

  