# amazonInterview

Most Popular questions in last 6 months 
- Count Unique Characters of All Substrings of a Given String (check -- not optimal though) 
- Reorder Data in Log Files (check)
- Search Suggestions System	
- LRU Cache
  - ########### IDEA: ##################
What is node? Node is just an object that stores key and its associated value. It has prev, next pointers. 
What is cache? maps key to node that contains key & value 
What is self.left, self.right? They indicate pointers of LRU and MRU in LL.
What is LL? keeps relative ordering of nodes based on LRU policy. 

remove(node): removes node from the LL that keeps track of relative order of (key, value) nodes based on LRU policy 

insert(node): inserts node from the right in the LL so that the node is most recently used. 

get(key): purpose is to return return cache[key].val if key exists in cache else return -1.
    Make sure to remove cache[key] in LL and add to LL.

put(key, value): purpose is to insert the new node with key & value in cache. 
    First, it checks if key exists in cache. If it does, remove key to node mapping from the cache (and from LL).
    Then, add node with key & value to the cache (and to LL). 
    If cache overflows, remove LRU from the cache (and from LL).
- Maximum Units on a Truck (X) 
- Count Binary Substrings (X) 
- Flip String to Monotone Increasing (X)
- The kth Factor of n (X) 
- Analyze User Website Visit Pattern (X) 

Most Popular questions in last 1 year 
- Robot Bounded In Circle (X)
- Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
- Maximum Units on a Truck (X)
- Minimum Cost to Connect Sticks (X)
- Concatenated Words
- Number of Islands (X) 


Most Popular Questions in last 2 years 
- Critical Connections in a Network (DO) 
- Number of Islands (X) 
- Partition Labels
- Rotting Oranges (X) 
- Top K Frequent Words (X) 
- Minimum Difficulty of a Job Schedule 
- Prison Cells After N Days 
- Most Common Word (X) 
- Word Ladder
- Find Median from Data Stream (X)
- LFU Cache
- Merge k Sorted Lists (X) 
- Copy List with Random Pointer (X)

