class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = {}
        for s in strs: 
            sort = "".join(sorted(s))
            if sort not in anagrams: 
                anagrams[sort] = [s]
            else: 
                anagrams[sort].append(s)
        return anagrams.values()
