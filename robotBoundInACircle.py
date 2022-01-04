'''
idea: 
Key: 

robot is guaranteed to be in a cycle if position is back at origin or dx, dy is not the same direction as it first started out. 
'''
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        
        dx, dy = 0, 1 #robot goes in the north direction 
        x, y = 0, 0 # current position
        
        for d in instructions: 
            if d == "G": 
                x, y = x + dx, y + dy 
            elif d == "L":
                # i.e. dx = -1, dy = 0 after turning 90 degrees left 
                dx, dy = dy*-1, dx #change direction
            elif d == "R":
                # i.e. dx = 1, dy = 0 after turning 90 degrees right 
                dx, dy = dy, dx*-1 #change direction 
        
        return (x, y) == (0, 0) or (dx, dy) != (0, 1)
