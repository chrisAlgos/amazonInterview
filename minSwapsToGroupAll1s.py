'''

Technique: sliding window where window is fixed and it's the number of 1s. 
Number of zeros in sliding window = number of swaps we must perform for that window. 




windowSize = sum(data) # window = number of 1s 
# for each window, get number of zeros in that window and update minSwaps 
minSwaps = float('inf')
for i in range(len(data)-windowSize+1): 
    currWindow = data[i:i+windowSize] 
    numZeros = windowSize - sum(currWindow)
    minSwaps = min(minSwaps, numZeros)
return minSwaps
'''


class Solution:
    def minSwaps(self, data: List[int]) -> int:
        
        
        windowSize = sum(data) # window = number of 1s 
        
        # initialize zeros and minSwaps in the current window from i = 0 to i = windowSize-1
        zeros = minSwaps = windowSize - sum(data[:windowSize])
        
        for i in range(windowSize, len(data)): 
            if data[i] == 0: # zero going into sliding window 
                zeros +=1 
            if data[i-windowSize] == 0: 
                zeros -=1 # zero going out of sliding window (out of bounds)
            minSwaps = min(minSwaps, zeros)
        return minSwaps
