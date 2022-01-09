class Solution:
        
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        '''
        updates = [[1,3,2],[2,4,3],[0,2,-2]]
        [0, 0, 0, 0, 0]
           +2       -2
              +3      
        -2        +2
        
        Technique: prefix sum (use this when you are summing over range multiple times)
        1. for each update: mark increment in the start index and its opposite (val*-1) in the end+1 index 
            [-2, 2, 3, 2, -2]
        2. Then, starting from index 1, update the arr[i] = arr[i] + arr[i-1]
        '''
        arr = [0 for _ in range(length)]
        #1. for each update: mark increment in the start index and its opposite (val*-1) in the end+1 index 
        for update in updates: 
            start, end, val = update 
            arr[start] += val 
            if end+1 < length: 
                arr[end+1] += (val*-1) # offsets increment for current index in arr so that increment is not applied to current sum (when calculating prefix sum) and for all sums after it 
                
        #2. Then, starting from index 1, update the arr[i] = arr[i] + arr[i-1]
        for i in range(1, length): #prefix sum 
            arr[i] += arr[i-1]
        
        return arr 
