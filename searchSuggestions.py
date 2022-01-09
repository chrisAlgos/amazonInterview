'''
Every time you type letter, get 3 strings from products that start with the string up to that letter and return list of lists. 
'''
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        products.sort() 
        
        res = []
        for i in range(1, len(searchWord)+1): 
            new = []
            prefix = searchWord[:i]
            for product in products: 
                if product.startswith(prefix): 
                    new.append(product)
                if len(new) == 3: 
                    break
            res.append(new)
        return res
 
'''
<b> searchSuggestions </b> 
- 1. sort products 
- 2. loop through searchWord from the 1st index up to len(searchWord)+1 (exclusive) and get prefix 
  - i. prefix = searchWord[:i] and loop through each product in products. If product.startswith(prefix), then add to lst. 
  - ii. Break out of loop if len(lst) == 3, and add lst to res 
'''
