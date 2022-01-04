'''
https://leetcode.com/problems/flip-string-to-monotone-increasing

Get minimum number of flips to get a monotone increasing string composed of 0s and 1s. 
s = "00110" --> 1 ("00111")
s = "010110" --> 2 ("011111")
s = "00011000" --> 2 ("00000000")
'''
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:

        flips, numOfOnes = 0, 0 
        
        for char in s: 
            
            if char == "0": 
                if numOfOnes == 0: 
                    # skip trailing zeros starting from left
                    continue  
                else: 
                    # we found "0" after "1" so we must flip 0 -> 1
                    flips += 1
            elif char == "1": 
                numOfOnes += 1
            
            # record changes that we have to make 
            # What is the minimum number of flips? 
            # flip all 1s to 0s OR flip 0s we got after encountering at least one 1? 
            flips = min(flips, numOfOnes)
        return flips
