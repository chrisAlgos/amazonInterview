class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        '''
        1. create freq dictionary
        2. create min heap with (least freq, value) 
        3. return number of elements in heap after k removals 
        '''
        # 1. create freq dictionary
        freq = {}
        for num in arr: 
            freq[num] = freq.get(num, 0)+1 
        
        # 2. create min heap with (least freq, value)
        heap = []
        for num, freq in freq.items(): 
            heapq.heappush(heap, (freq, num))
        
        # 3. return number of elements in heap after k removals 
        while k: 
            freq, num = heapq.heappop(heap)
            if freq - min(freq, k): 
                heapq.heappush(heap, (freq - min(freq, k), num))
            k -= min(freq, k)
        
        return len(heap)
