'''
Return the kth factor of n. 

Input: n = 12, k = 3
Output: 3
Explanation: Factors list is [1, 2, 3, 4, 6, 12], the 3rd factor is 3.


Input: n = 4, k = 4
Output: -1
Explanation: Factors list is [1, 2, 4], there is only 3 factors. We should return -1.
'''
class Solution:
    def kthFactor(self, n: int, k: int) -> int:

        factorsList = [i for i in range(1, n+1) if n%i==0]
    
        return -1 if len(factorsList) < k else factorsList[k-1]
