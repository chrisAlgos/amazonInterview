'''
return 2 indices whose elements sum to target 
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        numToIndex = {}
        
        for i in range(len(nums)): 
            
            complement = target - nums[i]
            
            if complement in numToIndex: 
                return [numToIndex[complement], i]
            else: 
                numToIndex[nums[i]] = i
