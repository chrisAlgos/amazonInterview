'''
idea: 
1. create max heap keyed on number of units per box; tuple=(units*-1, numBoxes)
2. keep updating maxUnits by adding units*numBoxes while number of boxes does not exceed truckSize threshold
'''
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        
        # boxTypes = number of boxes, number of units per box
        # truckSize = number of boxes cannot exceed truckSize 
        
        # 1. create max heap keyed on number of units per box
        heap = []
        for box in boxTypes: 
            numBoxes, units  = box 
            heapq.heappush(heap, (units*-1, numBoxes))
         
        # 2. keep updating maxUnits by adding (units*-1)*numBoxes while number of boxes does not exceed truckSize threshold and while there are elements in the heap.
        maxUnits = 0 
        while truckSize and heap: 
            units, numBoxes = heapq.heappop(heap) # pop box with max units 
            numBoxes = min(truckSize, numBoxes)
            maxUnits += (units*-1)*numBoxes # note maxUnits 
            truckSize -= numBoxes 
            numBoxes -= numBoxes 
            if numBoxes != 0: 
                heapq.heappush(heap, (units, numBoxes)) # put tuple (units, numBoxes) back into heap iff numBoxes != 0
            
        return maxUnits
        
