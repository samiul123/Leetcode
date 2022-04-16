class Solution:
    def isValid(self, s: str) -> bool:
        charMap = {')': '(', '}':'{', ']':'['}
        
        stack = []
        
        for char in s:
            if char not in charMap:
                stack.append(char)
                continue
            top = stack.pop() if stack else '$'
            if top != charMap[char]:
                return False
        
        return not stack
            
        
#         stack = []
        
#         # 
        
#         for char in s:
#             if char == "(" or char == "{" or char == "[":
#                 stack.append(char)
#             else:
#                 if len(stack) == 0:
#                     return False
#                 elif (stack[len(stack)-1] == "(" and char == ")") or (stack[len(stack)-1] == "{" and char == "}") or (stack[len(stack)-1] == "[" and char == "]"):
#                     stack.pop()
#                 else:
#                     return False
        
#         if len(stack) != 0:
#             return False
        
#         return True