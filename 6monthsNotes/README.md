<b> LRU cache </b> 
- What is node? Node is just an object that stores key and its associated value. It has prev, next pointers. 
- What is cache? maps key to node that contains key & value 
- What is self.left, self.right? They indicate pointers of LRU and MRU in LL.
- What is LL? keeps relative ordering of nodes based on LRU policy. 

- remove(node): removes node from the LL that keeps track of relative order of (key, value) nodes based on LRU policy 

- insert(node): inserts node from the right in the LL so that the node is most recently used. 

- get(key): purpose is to return return cache[key].val if key exists in cache else return -1.
    Make sure to remove cache[key] in LL and add to LL.

- put(key, value): purpose is to insert the new node with key & value in cache. 
    First, it checks if key exists in cache. If it does, remove key to node mapping from the cache (and from LL).
    Then, add node with key & value to the cache (and to LL). 
    If cache overflows, remove LRU from the cache (and from LL).


<b> searchSuggestions </b> 
- 1. sort products 
- 2. loop through searchWord from the 1st index up to len(searchWord)+1 (exclusive) and get prefix 
  - i. prefix = searchWord[:i] and loop through each product in products. If product.startswith(prefix), then add to lst. 
  - ii. Break out of loop if len(lst) == 3, and add lst to res 
