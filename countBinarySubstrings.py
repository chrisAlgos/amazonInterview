'''
Given a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's.

https://www.youtube.com/watch?v=4nVUaNGgfl0

Input: s = "00110011"
Output: 6
Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".

Idea: 

1. Initialize count of substrings = 0, prevBlockSize = 0, and currBlockSize = 1 
2. start loop through string from index 1. 
    - If the previous character is same to current character, then increment currBlockSize 
    - If the previous character is not the same, 
        - # of substrings that have the same number of 0's and 1's is the minimum of prevBlockSize and currBlockSize so add the min size to count 
        - prevBlockSize becomes currBlockSize 
        - reset currBlockSize to 1
3. Need to account for last case, so add min(prevBlockSize, currBlockSize) to count 
'''
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        
        count, prevBlockSize, currBlockSize = 0, 0, 1 # sizes of current block and previous block 

        for i in range(1, len(s)):
            if s[i] == s[i-1]: 
                currBlockSize += 1 
            else: 
                # i.e. 00011 where prevBlock = 000 and currBlock = 11 means there are 2 binary substrings
                count += min(prevBlockSize, currBlockSize)
                prevBlockSize = currBlockSize 
                currBlockSize = 1
        count += min(prevBlockSize, currBlockSize)
        return count
