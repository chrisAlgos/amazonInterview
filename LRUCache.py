'''
https://leetcode.com/problems/lru-cache/
(MUST) 
https://www.youtube.com/watch?v=7ABFKPK2hD4

What is node? Node is just an object that stores key and its associated value. It has prev, next pointers. 
What is cache? maps key to node that contains key & value 
What is self.left, self.right? They indicate pointers of LRU and MRU 
What is LL? keeps relative ordering of nodes based on LRU policy. 

remove(node): removes node from the LL that keeps track of relative order of (key, value) nodes based on LRU policy 

insert(node): inserts node from the right in the LL so that the node is most recently used. 

get(key): purpose is to return return cache[key].val if key exists in cache else return -1.
    Make sure to remove cache[key] in LL and add to LL.

put(key, value): purpose is to insert the new node with key & value in cache. 
    First, it checks if key exists in cache. If it does, remove key to node mapping from the cache (and from LL).
    Then, add node with key & value to the cache (and to LL). 
    If cache overflows, remove LRU from the cache (and from LL).
'''
class Node: 
    def __init__(self, key, val): 
        self.key, self.val = key, val 
        self.prev = self.next = None 
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.cache = {}
        # left = LRU, right = most recently used 
        self.left, self.right= Node(0, 0), Node(0, 0) #let them point to dummy nodes first 
        self.left.next, self.right.prev = self.right, self.left
    
    def remove(self, node): # remove node from list 
        prev, nxt = node.prev, node.next 
        prev.next, nxt.prev = nxt, prev
    
    def insert(self, node): # insert node at right 
        prev, nxt = self.right.prev, self.right
        prev.next, nxt.prev = node, node
        node.prev, node.next = prev, nxt
    
    def get(self, key: int) -> int:
        if key in self.cache: 
            self.remove(self.cache[key]) # remove node from the list
            self.insert(self.cache[key]) # insert it to the right since it's most recently used 
            return self.cache[key].val 
        return -1 # node does not exist in list

    def put(self, key, value): 
        if key in self.cache: # key already exists in cache
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        
        if len(self.cache) > self.capacity: 
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]
            
