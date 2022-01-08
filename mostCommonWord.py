'''
get most common word in the given string that is not in the banned list
'''
class Solution:
    
    # c.isalnum returns true if c is alphabetic or numeric 
    def process(self, paragraph): 
        paragraph = ''.join([c if c.isalnum() else ' ' for c in paragraph.lower()])
        paragraph = paragraph.split(" ")
        return paragraph
            
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        paragraph = self.process(paragraph) # returns array of valid words in the paragraph 
        counter, banned = {}, set(banned)
        for word in paragraph: # get frequency of each word 
            if word in banned or word == '': continue # if word is in banned list or if word = ''
            counter[word] = counter.get(word, 0) + 1

        return max(counter.items(), key=operator.itemgetter(1))[0]
