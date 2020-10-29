class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) > 0:
        
            from itertools import product

            keybord = {
                1: '', 2: 'abc', 3: 'def',
                4: 'ghi', 5: 'jkl', 6: 'mno',
                7: 'pqrs', 8: 'tuv', 9: 'wxyz'
            }
        
            numbers = [keybord[int(i)] for i in digits]
            combinations_tuples = product(*numbers)
        
            result = []
        
            for combination in combinations_tuples:
                result.append(''.join(combination))    
        
            return result

        else: 
            return []