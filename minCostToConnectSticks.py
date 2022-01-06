'''
Minimum Cost to Connect Sticks
Time: We make N heappush 
Space: heap will contain N elements at any given time

Time | Space = O(NlogN) | O(N) 
Input: sticks = [2,4,3]
Output: 14
Explanation: You start with sticks = [2,4,3].
1. Combine sticks 2 and 3 for a cost of 2 + 3 = 5. Now you have sticks = [5,4].
2. Combine sticks 5 and 4 for a cost of 5 + 4 = 9. Now you have sticks = [9].
There is only one stick left, so you are done. The total cost is 5 + 9 = 14.
'''
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        
        heap = []
        for stick in sticks: 
            heapq.heappush(heap, stick)
            
        minCost = 0 
        while len(heap) > 1: 
            stick1, stick2 = heapq.heappop(heap), heapq.heappop(heap)
            stickSum = stick1 + stick2
            minCost += stickSum
            heapq.heappush(heap, stickSum)

        return minCost
            
