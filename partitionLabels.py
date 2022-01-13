class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        endIndices = {ch:i for i, ch in enumerate(s)}
        res,i = [],0 
        
        # loop through string s
        while i < len(s): 
            
            # 1. get endIdx of i-th character
            endIdx = endIndices[s[i]] if endIndices[s[i]] > i else i
            
            # 2. keep updating endIdx if the current character s[k] has index greater than endIdx 
            k = i+1
            while k < endIdx:
                endIdx = endIndices[s[k]] if endIndices[s[k]] > endIdx else endIdx
                k+=1 
                
            # 3. append length to res 
            res.append(endIdx-i+1)
            
            # 4. update i to start from endIdx+1
            i = endIdx+1
            
        return res
            
