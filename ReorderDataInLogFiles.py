'''
Reorder Data in Log Files

https://leetcode.com/problems/reorder-data-in-log-files

letter logs: everything else are letters
digit logs: everything else are digits

return letters + digits 

where digits keep relative ordering 
where letters are sorted by identifier IFF the rest are the same
'''

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        # divide into digits and letters
        digits, letters = [], []
        
        for log in logs: 
            arr = log.split(" ")
            if arr[1].isdigit(): 
                digits.append(log)
            else: # letter 
                letters.append(log)
        
        letters.sort(key=lambda x: x.split(" ")[0])
        letters.sort(key=lambda x: x.split(" ")[1:])
        
        return letters+digits
