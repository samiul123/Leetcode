class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        configDict = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        combinations = []
        
        def findCombinations(idx, combination):
            if len(combination) == len(digits):
                combinations.append("".join(combination))
                return
              
            letters = configDict[digits[idx]]
            for i in range(len(letters)):
                combination.append(letters[i])
                findCombinations(idx + 1, combination)
                combination.pop()
        
        findCombinations(0, [])
        
        return combinations
        
        