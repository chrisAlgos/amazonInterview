"""
138. Copy List with Random Pointer

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        oldToCopy = {None: None} 
        # 1. create a hashmap oldToCopy
        curr = head 
        while curr: 
            oldToCopy[curr] = Node(curr.val) #old node maps to copy node
            curr = curr.next 
        
        # 2. using oldToNew, enter a while curr exists, and set copy's pointers 
        curr = head 
        while curr: 
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next 
        
        return oldToCopy[head]
    
