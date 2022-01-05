
'''
https://www.youtube.com/watch?v=4nVUaNGgfl0

Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
'''
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        count, prevBlock, currBlock = 0, 0, 1 # sizes of current block and previous block 
        #current = s[0]
        for i in range(1, len(s)):
            if s[i] == s[i-1]: 
                currBlock += 1 
            else: 
                # i.e. 00011 where prevBlock = 000 and currBlock = 11 means there are 2 binary substrings
                count += min(prevBlock, currBlock)
                prevBlock = currBlock 
                currBlock = 1 
            #current = s[i]
        
        count += min(prevBlock, currBlock)
        return count
