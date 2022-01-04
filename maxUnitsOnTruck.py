'''
(MUST)
https://leetcode.com/problems/maximum-units-on-a-truck/
'''
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        
        heap = []
        
        for i in range(len(boxTypes)): 
            tup = (boxTypes[i][1]*-1, i, boxTypes[i][0])
            heap.append(tup)
        heapq.heapify(heap)
        
        maxUnits = 0 
        while truckSize and len(heap) != 0: 
            units, i, num = heapq.heappop(heap)
            units *= -1
            
            if num < truckSize: 
                truckSize -= num
                maxUnits += (units*num)
                num = 0 
            else: 
                num -= truckSize 
                maxUnits += units*(truckSize)
                truckSize = 0  
                
            if num != 0: 
                heapq.heappush(heap, (units*-1, i, num))
        
        return maxUnits 
