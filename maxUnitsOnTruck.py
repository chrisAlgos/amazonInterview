class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        
        print(boxTypes, truckSize) # # of boxes, number of units in each box
        # truckSize = number of boxes cannot exceed truckSize 

        heap = []
        
        for box in boxTypes: 
            numBoxes, units  = box 
            heapq.heappush(heap, (units*-1, numBoxes))
            
        maxUnits = 0 
        while truckSize and heap: 
            units, numBoxes = heapq.heappop(heap)
            numBoxes = min(truckSize, numBoxes)
            maxUnits += (units*-1)*numBoxes
            truckSize -= numBoxes
            numBoxes -= numBoxes 
            if numBoxes != 0: 
                heapq.heappush(heap, (units, numBoxes))
            
        return maxUnits
        
