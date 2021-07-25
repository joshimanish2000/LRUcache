# LRUcache
Implement a Least Recently Used Cache page replacement algorithm with Python.
The implementation is based on a Positional Linked List which allows constant time (O(1)) insertions and deletions at arbitrary locations. 
A dictionary is used to map page names to their locations in the the cache. Cache stores web addresses of the websites. 
Cache size is limited by the max_size attribute. If cache is full and a new insertion is to be made, the page whose last request was made furthest in the past is evicted to make room.
When a page is accessed, it is put at the top of the cache in anticipation that it will be accessed again soon.

