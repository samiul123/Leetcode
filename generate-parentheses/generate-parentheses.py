class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open, close = 0, 0
        combinations = []
        
        def recurse(open, close, combination):
            if open == close == n:
                combinations.append("".join(combination))
                return
            
            if open < n:
                combination.append("(")
                recurse(open+1, close, combination)
                combination.pop()
            if close < open:
                combination.append(")")
                recurse(open, close+1, combination)
                combination.pop()
                
        recurse(open, close, [])
        return combinations
        